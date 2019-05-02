import string
from itertools import product

import requests
from bs4 import BeautifulSoup

from course import course


def preparePackage(SEM, FAC):
    """Preparing package with given semseter and faculty in order to get courses from UG

    Args:
        SEM (INT): semester number (eg. "201802")
        FAC (INT): faculty  number parsed from UG html 
    """
    postPackage = {
        'CNM': '',
        'CNO': '',
        'PNT': '',
        'LLN': '',
        'LFN': '',
        'RECALL': 'Y',
        'D1': 'on',
        'D2': 'on',
        'D3': 'on',
        'D4': 'on',
        'D5': 'on',
        'D6': 'on',
        'FTM': '',
        'TTM': '',
        'SIL': '',
        'OPTCAT': 'on',
        'OPTSEM': 'on',
        'doSearch': 'Y',
        'Search': 'חפש',
        'FAC': FAC,
        'SEM': SEM
    }
    return postPackage


def getCourses(url, postPackage):
    with requests.Session() as session:
        get = session.post(url, data=postPackage)
        soup = BeautifulSoup(get.content, features="html5lib")
        selects = soup.find_all(lambda a: a.has_attr('href'))
        return uniqueAndSortInput(selects, "content")


def getData(url, tag, attrs, types):
    # //TODO : Get old one working aswell
    with requests.Session() as session:
        get = session.post(url)
        soup = BeautifulSoup(get.content, features="html5lib")
        selects = soup.find_all(tag, attrs)
        return uniqueAndSortInput(selects, types)


def uniqueAndSortInput(selects, part):
    sem = set()
    for a in selects:
        if part == "values":
            if a.attrs != {}:
                for val in a.attrs.values():
                    try:
                        int(val)
                    except ValueError:
                        continue
                    sem.add(int(val))
        if part == "content":
            try:
                sem.add(int(a.contents[0]))
            except IndexError:
                continue
            except TypeError:
                continue
            except ValueError:
                continue
        if part == "course":
            return selects #TODO: maybe split this to another page
    return sorted(sem)


def getCourseInfo(course_number, semester):
    url = "https://ug3.technion.ac.il/rishum/course/" + \
        str(course_number) + "/" + str(semester)
    tag = "div"
    attrs = {"class": "property"}
    types = "course"
    properties = getData(url, tag, attrs, types)
    strip = "".maketrans({"\n": None, "\r": None, "\t": None, "\xa0": " "})
    white_spaces = "".maketrans({" ": None})
    and_trans = "".maketrans({"ו": None, "-": "&"})
    or_trans = "".maketrans({"א": "|", "-": None})
    temp_course = course()
    for prop in properties:
        # TODO: Parse courses in dependencies etc one by one
        if "שם מקצוע" in prop.text:
            temp_course.set_name(prop.next_sibling.next_sibling.text.translate(strip))
        if "מספר מקצוע" in prop.text:
            temp_course.set_number(prop.next_sibling.next_sibling.text.translate(
                    strip).translate(white_spaces))
        if "נקודות" in prop.text:
            temp_course.set_points(prop.next_sibling.next_sibling.text.translate(
                    strip).translate(white_spaces))
        if "מקצועות קדם" in prop.text:
            temp_course.add_dependencies(prop.next_sibling.next_sibling.text.translate(
                    strip).translate(and_trans).translate(or_trans))
        if "מקצועות צמודים" in prop.text:
            temp_course.add_parallel(prop.next_sibling.next_sibling.text.translate(strip))
        if ":מקצועות ללא זיכוי נוסף" in prop.text:
            temp_course.add_similarities(prop.next_sibling.next_sibling.text.translate(strip))
        if "מקצועות ללא זיכוי נוסף (מוכלים)" in prop.text:
            temp_course.add_inclusive(prop.next_sibling.next_sibling.text.translate(strip))
    return temp_course


def prepareCourses():
    semester_tag = "input"
    semester_attrs = {"type": "radio", "name": "SEM"}
    faculties_tag = "option"
    faculties_attrs = {}
    search_url = 'https://ug3.technion.ac.il/rishum/search'
    semesters = getData(search_url, semester_tag, semester_attrs, "values")
    faculties = getData(search_url, faculties_tag, faculties_attrs, "values")
    packages = []
    for combination in product(semesters, faculties):
        packages.append(preparePackage(combination[0], combination[1]))
    course_numbers = set()
    for package in packages:
        for course in getCourses(search_url, package):
            course_numbers.add(course)
    courses = list()
    for course_number in sorted(course_numbers):
        courses.append(getCourseInfo(course_number, semesters[len(semesters) - 1]))
    a = 1

prepareCourses()
