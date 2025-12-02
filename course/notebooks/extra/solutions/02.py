import ROOT

# Filter using a C++ expression string instead of a Python lambda
filteredEvents = (
    rdf.Filter("Q1 * Q2 < 0")  # opposite charges
       .Define(
           "m",
           "sqrt(pow(E1 + E2, 2) - (pow(px1 + px2, 2) + "
           "pow(py1 + py2, 2) + pow(pz1 + pz2, 2)))"
       )
)

invMass = filteredEvents.Histo1D(
    ("invMass",
     "CMS Opendata: #mu^{-}#mu^{+} mass;#mu^{-}#mu^{+} mass / GeV/c^{2};Events",
     512, 2, 110),
    "m",
)

%jsroot on
c = ROOT.TCanvas("c_invMass", "dimuon mass", 800, 600)
c.SetLogy()
c.SetLogx()
invMass.Draw()
c.Draw()