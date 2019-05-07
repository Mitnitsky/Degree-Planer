from PyQt5 import QtCore, QtGui, QtWidgets


class ComboBoxDelegate(QtWidgets.QStyledItemDelegate):
    """ComboBox view inside of a Table. It only shows the ComboBox when it is
       being edited.
    """

    def __init__(self, model, itemlist=None):
        super().__init__(model)
        self.model = model
        self.itemlist = None

    # end Constructor

    def createEditor(self, parent, option, index):
        """Create the ComboBox editor view."""
        if self.itemlist is None:
            self.itemlist = self.model.getItemList(index)

        editor = QtWidgets.QComboBox(parent)
        editor.addItems(self.itemlist)
        editor.setCurrentIndex(0)
        editor.installEventFilter(self)
        return editor

    # end createEditor

    def setEditorData(self, editor, index):
        """Set the ComboBox's current index."""
        value = index.data(QtCore.Qt.DisplayRole)
        i = editor.findText(value)
        if i == -1:
            i = 0
        editor.setCurrentIndex(i)

    # end setEditorData

    def setModelData(self, editor, model, index):
        """Set the table's model's data when finished editing."""
        value = editor.currentText()
        model.setData(index, value)

    # end setModelData


# end class ComboBoxDelegate
