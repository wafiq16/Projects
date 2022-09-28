#include "mainwindow.h"
#include "logindialog.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    LoginDialog login;
    login.setWindowTitle("app");
    login.show();

//    MainWindow mainWindow;
//    mainWindow.setWindowTitle("app");
//    mainWindow.show();
    return a.exec();
}
