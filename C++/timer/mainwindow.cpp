#include "mainwindow.hh"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    minutes = 0;
    seconds = 0;

    timer = new QTimer(this);
    connect(timer, SIGNAL(timeout()), this, SLOT(updateTimer()));

    connect(ui->startButton, SIGNAL(clicked()), this, SLOT(startTimer()));
    connect(ui->stopButton, SIGNAL(clicked()), this, SLOT(stopTimer()));
    connect(ui->resetButton, SIGNAL(clicked()), this, SLOT(resetTimer()));
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::startTimer()
{
    if (!timer->isActive()) {
        timer->start(1000);
    }
}

void MainWindow::stopTimer()
{
    if (timer->isActive()) {
        timer->stop();
    }
}

void MainWindow::resetTimer()
{
    timer->stop();
    minutes = 0;
    seconds = 0;
    updateTimer();
}

void MainWindow::updateDisplay()
{
    ui->lcdNumberMin->display(minutes);
    ui->lcdNumberSec->display(seconds);
}

void MainWindow::updateTimer()
{
    seconds++;
    if (seconds == 60) {
        minutes++;
        seconds = 0;
    }
    updateDisplay();
}
