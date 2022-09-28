#include "logindialog.h"
#include "ui_logindialog.h"


LoginDialog::LoginDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::LoginDialog)
{
    ui->setupUi(this);
}

LoginDialog::~LoginDialog()
{
    delete ui;
}

void LoginDialog::on_login_clicked()
{
    Qusername = ui->username->text();
    username = Qusername.toUtf8().constData();

    Qpassword = ui->password->text();
    password = Qpassword.toUtf8().constData();

    if(!strcmp(username.c_str(), "admin") && !strcmp(password.c_str(),"admin")){
//        login handler
        cout << "user benar pass benar" << endl;
        QMessageBox msgBox;
        msgBox.setText("Welcome back sir !!!.");
        msgBox.exec();

        this->close();

        mainWindow.setWindowTitle("app");
        mainWindow.show();
    }
    else{
//            incorect input
        cout << "user salah atau pass salah" << endl;
        QMessageBox msgBox;
        msgBox.setText("Please input right username and password !!!.");
        msgBox.exec();
    }
}
