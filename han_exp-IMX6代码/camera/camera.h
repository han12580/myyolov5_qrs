#ifndef CAMERA_H
#define CAMERA_H

#include <QWidget>
#include <QMovie>
#include <QTimer>
#include<QImage>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#include <getopt.h>

#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <malloc.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/time.h>
#include <sys/mman.h>
#include <sys/ioctl.h>

#include <QTcpSocket>
#include <QHostAddress>
#include <asm/types.h>
#include <linux/videodev2.h>
#include "camerathread.h"

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
namespace Ui {
class camera;
}

class camera : public QWidget
{
    Q_OBJECT

public:
    explicit camera(QWidget *parent = 0);
    ~camera();

private slots:
    void on_startButton_clicked();

private:
    Ui::camera *ui;

public:
    bool cameraflag;
    QImage frame;
    qint64 totalBytes;    // 发送数据的总大小
    QTcpSocket *tcpClient;
    QByteArray outBlock;
    person sendImage(QImage frame);
public:
    cameraThread *camerathread;

signals:
       void Show_complete();


private slots:
    void videoDisplay(unsigned char *pp);
    void errorshowslot();


};

#endif // CAMERA_H
