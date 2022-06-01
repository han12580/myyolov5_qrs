#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include<qbuffer.h>
#include<qtcpsocket.h>
#include <QHostAddress>
namespace Ui {
class MainWindow;
}


struct person{
    int x;
    int y;
    int w;
    int h;
    QString name;
    person(int x1,int y1,int w1,int h1,QString name1)
    {
        x=x1;
        y=y1;
        w=w1;
        h=h1;
        name=name1;
    }
};



class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    QTcpSocket *t;
    QImage frame;
    ~MainWindow();
    void sendIamge();
    qint64 totalBytes;
    QByteArray outBlock;
    person pe;

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
