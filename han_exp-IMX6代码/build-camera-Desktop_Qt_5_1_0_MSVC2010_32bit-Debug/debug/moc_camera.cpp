/****************************************************************************
** Meta object code from reading C++ file 'camera.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.1.0)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../camera/camera.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'camera.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.1.0. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
struct qt_meta_stringdata_camera_t {
    QByteArrayData data[8];
    char stringdata[91];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    offsetof(qt_meta_stringdata_camera_t, stringdata) + ofs \
        - idx * sizeof(QByteArrayData) \
    )
static const qt_meta_stringdata_camera_t qt_meta_stringdata_camera = {
    {
QT_MOC_LITERAL(0, 0, 6),
QT_MOC_LITERAL(1, 7, 13),
QT_MOC_LITERAL(2, 21, 0),
QT_MOC_LITERAL(3, 22, 22),
QT_MOC_LITERAL(4, 45, 12),
QT_MOC_LITERAL(5, 58, 14),
QT_MOC_LITERAL(6, 73, 2),
QT_MOC_LITERAL(7, 76, 13)
    },
    "camera\0Show_complete\0\0on_startButton_clicked\0"
    "videoDisplay\0unsigned char*\0pp\0"
    "errorshowslot\0"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_camera[] = {

 // content:
       7,       // revision
       0,       // classname
       0,    0, // classinfo
       4,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    0,   34,    2, 0x05,

 // slots: name, argc, parameters, tag, flags
       3,    0,   35,    2, 0x08,
       4,    1,   36,    2, 0x08,
       7,    0,   39,    2, 0x08,

 // signals: parameters
    QMetaType::Void,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void, 0x80000000 | 5,    6,
    QMetaType::Void,

       0        // eod
};

void camera::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        camera *_t = static_cast<camera *>(_o);
        switch (_id) {
        case 0: _t->Show_complete(); break;
        case 1: _t->on_startButton_clicked(); break;
        case 2: _t->videoDisplay((*reinterpret_cast< unsigned char*(*)>(_a[1]))); break;
        case 3: _t->errorshowslot(); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        void **func = reinterpret_cast<void **>(_a[1]);
        {
            typedef void (camera::*_t)();
            if (*reinterpret_cast<_t *>(func) == static_cast<_t>(&camera::Show_complete)) {
                *result = 0;
            }
        }
    }
}

const QMetaObject camera::staticMetaObject = {
    { &QWidget::staticMetaObject, qt_meta_stringdata_camera.data,
      qt_meta_data_camera,  qt_static_metacall, 0, 0}
};


const QMetaObject *camera::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *camera::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_camera.stringdata))
        return static_cast<void*>(const_cast< camera*>(this));
    return QWidget::qt_metacast(_clname);
}

int camera::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 4)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 4;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 4)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 4;
    }
    return _id;
}

// SIGNAL 0
void camera::Show_complete()
{
    QMetaObject::activate(this, &staticMetaObject, 0, 0);
}
QT_END_MOC_NAMESPACE
