#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include "THStack.h"
#include "TH1F.h"
#include "TCanvas.h"
#include "TLegend.h"

void plot_crc_and_bertest() {
    std::string file_name = "parsed_results.txt";

    // Vectors to store parsed data
    std::vector<int> cml_bias;
    std::vector<int> crc_errors;
    std::vector<int> crc_format_errors;
    std::vector<int> bertest_errors;

    std::ifstream file(file_name);
    if (!file.is_open()) {
        std::cerr << "Error opening file: " << file_name << std::endl;
        return;
    }

    std::string line;
    while (std::getline(file, line)) {
        if (line.find("DAC_CML_BIAS_0") != std::string::npos) {
            cml_bias.push_back(std::stoi(line.substr(line.find("=") + 1)));
        } else if (line.find("Total CRC Errors") != std::string::npos) {
            crc_errors.push_back(std::stoi(line.substr(line.find(":") + 1)));
        } else if (line.find("Total CRC Format Errors") != std::string::npos) {
            crc_format_errors.push_back(std::stoi(line.substr(line.find(":") + 1)));
        } else if (line.find("BERTest Frames with Errors") != std::string::npos) {
            bertest_errors.push_back(std::stoi(line.substr(line.find(":") + 1)));
        }
    }
    file.close();

    // same size vectors
    if (cml_bias.size() != crc_errors.size() ||
        cml_bias.size() != crc_format_errors.size() ||
        cml_bias.size() != bertest_errors.size()) {
        std::cerr << "Mismatch in data size!" << std::endl;
        return;
    }

    // sorting data
    std::vector<size_t> indices(cml_bias.size());
    std::iota(indices.begin(), indices.end(), 0);
    std::sort(indices.begin(), indices.end(), [&](size_t i, size_t j) { return cml_bias[i] < cml_bias[j]; });

    std::vector<int> sorted_cml_bias, sorted_crc_errors, sorted_crc_format_errors, sorted_bertest_errors;
    for (auto i : indices) {
        sorted_cml_bias.push_back(cml_bias[i]);
        sorted_crc_errors.push_back(crc_errors[i]);
        sorted_crc_format_errors.push_back(crc_format_errors[i]);
        sorted_bertest_errors.push_back(bertest_errors[i]);
    }

    // hists
    int n_bins = sorted_cml_bias.size();
    double bin_width = 1.0;

    TH1F* h_crc_errors = new TH1F("h_crc_errors", "CRC Errors", n_bins, 0, n_bins * bin_width);
    TH1F* h_crc_format_errors = new TH1F("h_crc_format_errors", "CRC Format Errors", n_bins, 0, n_bins * bin_width);
    TH1F* h_bertest_errors = new TH1F("h_bertest_errors", "BERTest Frames with Errors", n_bins, 0, n_bins * bin_width);

    //fill hists
    for (size_t i = 0; i < sorted_cml_bias.size(); ++i) {
        h_crc_errors->Fill(i, sorted_crc_errors[i]);
        h_crc_format_errors->Fill(i, sorted_crc_format_errors[i]);
        h_bertest_errors->Fill(i, sorted_bertest_errors[i]);
    }

    for (size_t i = 0; i < sorted_cml_bias.size(); ++i) {
        h_crc_errors->GetXaxis()->SetBinLabel(i + 1, std::to_string(sorted_cml_bias[i]).c_str());
        h_crc_format_errors->GetXaxis()->SetBinLabel(i + 1, std::to_string(sorted_cml_bias[i]).c_str());
        h_bertest_errors->GetXaxis()->SetBinLabel(i + 1, std::to_string(sorted_cml_bias[i]).c_str());
    }

    h_crc_errors->SetFillColor(kBlue);
    h_crc_format_errors->SetFillColor(kOrange);
    h_bertest_errors->SetFillColor(kGreen);

    THStack* stack = new THStack("stack", "CRC Errors and CRC Format Errors");
    stack->Add(h_crc_errors);
    stack->Add(h_crc_format_errors);

    TCanvas* c = new TCanvas("c", "CML Bias Tests", 800, 600);
    c->Divide(1, 2);

    c->cd(1);
    stack->Draw("bar");
    stack->GetXaxis()->SetTitle("CML Bias");
    stack->GetYaxis()->SetTitle("Error Counts");
    TLegend* legend1 = new TLegend(0.7, 0.8, 0.9, 0.9);
    legend1->AddEntry(h_crc_errors, "CRC Errors", "f");
    legend1->AddEntry(h_crc_format_errors, "CRC Format Errors", "f");
    legend1->Draw();

    c->cd(2);
    h_bertest_errors->Draw("bar");
    h_bertest_errors->GetXaxis()->SetTitle("CML Bias");
    h_bertest_errors->GetYaxis()->SetTitle("BERTest Errors");
    TLegend* legend2 = new TLegend(0.7, 0.8, 0.9, 0.9);
    legend2->AddEntry(h_bertest_errors, "BERTest Frames with Errors", "f");
    legend2->Draw();

    c->SaveAs("cml_bias_results.pdf");
    c->Draw();
}

