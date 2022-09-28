#ifndef LOGINDIALOG_H
#define LOGINDIALOG_H

#include <QDialog>
#include <QMessageBox>
#include <string.h>
#include <iostream>
#include <mainwindow.h>

using namespace std;

namespace Ui {
class LoginDialog;
}

class LoginDialog : public QDialog
{
    Q_OBJECT

public:
    explicit LoginDialog(QWidget *parent = nullptr);
    ~LoginDialog();

    // variable
    QString Qusername;
    QString Qpassword;
    string username;
    string password;

    MainWindow mainWindow;

private slots:

    void on_login_clicked();

private:
    Ui::LoginDialog *ui;
};

#endif // LOGINDIALOG_H
