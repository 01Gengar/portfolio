#include "mainwindow.hh"
#include "ui_mainwindow.h"
#include <iostream>
#include <fstream>
#include <string>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_findPushButton_clicked()
{
    QString resultText = "";

    QString fileName = ui->fileLineEdit->text();
    QString targetWord = ui->keyLineEdit->text();

    std::ifstream file(fileName.toStdString());

    if (!file.is_open()) {
        resultText = "File not found";
    } else if (targetWord.isEmpty()) {
        resultText = "File found";
    } else {
        std::string word;
        bool wordFound = false;
        bool caseSensitiveSearch = ui->matchCheckBox->isChecked();

        while (file >> word) {
            Qt::CaseSensitivity caseSensitivity = caseSensitiveSearch ? Qt::CaseSensitive : Qt::CaseInsensitive;
            if (QString::compare(QString::fromStdString(word), targetWord, caseSensitivity) == 0) {
                wordFound = true;
                break;
            }
        }

        if (wordFound) {
            resultText = "Word found";
        } else {
            resultText = "Word not found";
        }

        file.close();
    }

    ui->textBrowser->setText(resultText);
}
