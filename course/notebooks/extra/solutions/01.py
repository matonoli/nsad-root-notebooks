import ROOT
import numpy as np

# 1. Create and fill a histogram
h_ex = ROOT.TH1D("h_ex", "Exercise histogram; x; Events", 50, -5, 5)
h_ex.FillRandom("gaus", 5000)

# 2. Draw the histogram
%jsroot on
c1 = ROOT.TCanvas("c1", "Histogram", 600, 400)
h_ex.Draw()
c1.Draw()

# 3. Build a TGraph from the histogram
nbins = h_ex.GetNbinsX()
x = np.zeros(nbins, dtype=float)
y = np.zeros(nbins, dtype=float)

for i in range(1, nbins + 1):   # bin numbering starts at 1
    x[i-1] = h_ex.GetBinCenter(i)
    y[i-1] = h_ex.GetBinContent(i)

g_ex = ROOT.TGraph(nbins, x, y)
g_ex.SetTitle("Bin centers vs contents; x; Events")
g_ex.SetMarkerStyle(20)
g_ex.SetLineColor(ROOT.kBlue)

# 4. Draw the graph
c2 = ROOT.TCanvas("c2", "Graph", 600, 400)
g_ex.Draw("AP")  # A = draw axes, P = draw points
c2.Draw()