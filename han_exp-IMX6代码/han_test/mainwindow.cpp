#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    this->t=new QTcpSocket(this);

    this->t->connectToHost("127.0.0.1",
                                 8080);
    this->sendIamge();

}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::sendIamge()
{
    while (1) {
        QPixmap pixmap = QPixmap::fromImage(QImage("E:/learn_deep/datasets/Cheng_Long/Cheng_Long_0001.jpg"));
        QByteArray ba;
        QBuffer buf(&ba);
        QString re;
        pixmap.save(&buf,"jpg");

        t->write(QString("size=%1").arg(ba.size()).toLocal8Bit().data());
        if(t->waitForReadyRead())
        {
            re=t->readAll();
            qDebug(re.toStdString().data());
        }

        qDebug(ba);
        t->write(ba);
        if(t->waitForReadyRead()){
            re=t->readAll();
            if(re=="no")
                return
            qDebug(re.toStdString().data());
            QStringList list=re.split(",");
            pe.x=list[0].toInt();
            pe.y=list[1].toInt();
            pe.w=list[2].toInt();
            pe.h=list[3].toInt();
            pe.name=list[4];
            qDebug(list[0].toStdString().data());
            qDebug(list[1].toStdString().data());
            qDebug(list[2].toStdString().data());
            qDebug(list[3].toStdString().data());
            qDebug(list[4].toStdString().data());
        }

    }

}


