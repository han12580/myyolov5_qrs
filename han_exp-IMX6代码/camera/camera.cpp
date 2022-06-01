#include "camera.h"
#include "ui_camera.h"
#include <stdlib.h>




camera::camera(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::camera)
{
    ui->setupUi(this);

    tcpClient->connectToHost("192.168.5.88",
                                 8080);
    camerathread = new cameraThread();

    connect(camerathread, SIGNAL(errorshow()), this, SLOT(errorshowslot()));

    connect(this,SIGNAL(Show_complete()),camerathread,SLOT(startCapture()));
    connect(camerathread,SIGNAL(Collect_complete(unsigned char*)),this,SLOT(videoDisplay(unsigned char*)));
    camerathread->start();
}

camera::~camera()
{
    delete ui;
}

void camera::errorshowslot()
{
    ui->cameraLabel->setText(tr("摄像头初始化失败，请检查是否插好，并重新启动！"));
}

void camera::videoDisplay(unsigned char *pp)
{
    frame = QImage(pp,IMAGE_WIDTH,IMAGE_HEIGHT,QImage::Format_RGB888).mirrored(false, false);
    sendImage(frame);
    ui->cameraLabel->setPixmap(QPixmap::fromImage(frame));
}

void camera::on_startButton_clicked()
{
    cameraflag = cameraflag ? false : true;
    if(cameraflag == true)
    {
         ui->startButton->setText(tr("暂停"));
        emit this->Show_complete();
    }
    else
    {
       ui->startButton->setText(tr("播放"));
       emit this->Show_complete();
    }
}

person camera::sendImage(QImage frame)
{
    QPixmap pixmap = QPixmap::fromImage(frame);
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
            return NULL;
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
        return re;
    }
}
