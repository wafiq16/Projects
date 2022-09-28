#ifndef COBADIALOG_H
#define COBADIALOG_H

#include <QDialog>

namespace Ui {
class CobaDialog;
}

class CobaDialog : public QDialog
{
    Q_OBJECT

public:
    explicit CobaDialog(QWidget *parent = nullptr);
    ~CobaDialog();

private:
    Ui::CobaDialog *ui;
};

#endif // COBADIALOG_H
