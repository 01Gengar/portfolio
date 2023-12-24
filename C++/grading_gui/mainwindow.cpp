#include "mainwindow.hh"
#include "gradecalculator.hh"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    ui->spinBoxN->setRange(0, MAX_N_POINTS);
    ui->spinBoxG->setRange(0, MAX_G_POINTS);
    ui->spinBoxP->setRange(0, MAX_P_POINTS);
    ui->spinBoxE->setRange(0, 5);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_calculatePushButton_clicked()
{
    unsigned int n = ui->spinBoxN->value();
    unsigned int g = ui->spinBoxG->value();
    unsigned int p = ui->spinBoxP->value();
    unsigned int e = ui->spinBoxE->value();

    QString resultText = QString("W-Score: %1\nP-Score: %2\nTotal grade: %3")
                              .arg(QString::number(score_from_weekly_exercises(n, g)),
                                  QString::number(score_from_projects(p)),
                                  QString::number(calculate_total_grade(n, g, p, e)));

    ui->textBrowser->setText(resultText);
}
