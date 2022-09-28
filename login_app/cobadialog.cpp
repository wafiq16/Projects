#include "cobadialog.h"
#include "ui_cobadialog.h"

CobaDialog::CobaDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::CobaDialog)
{
    ui->setupUi(this);
}

CobaDialog::~CobaDialog()
{
    delete ui;
}
