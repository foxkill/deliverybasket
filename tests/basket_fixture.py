#
# dlv:tests:basket:fixture
#
import pytest
from unittest.mock import AsyncMock
from dlv.basket import Basket

@pytest.fixture
def create_basket(create_future, generate_cusips) -> Basket:
    tr = {t:None for t in generate_cusips}
    basket = Basket(tr)  # type: ignore
    return basket
# 'Object of type coroutine is not JSON serializable
@pytest.fixture
def response_for_912810TV0(): 
	# mo = AsyncMock()
	# mo.return_value 
	return [
		{
			"cusip": "912810TV0",
			"issueDate": "2024-01-16T00:00:00",
			"securityType": "Bond",
			"securityTerm": "29-Year 10-Month",
			"maturityDate": "2053-11-15T00:00:00",
			"interestRate": "4.750000",
			"refCpiOnIssueDate": "",
			"refCpiOnDatedDate": "",
			"announcementDate": "2024-01-04T00:00:00",
			"auctionDate": "2024-01-11T00:00:00",
			"auctionDateYear": "2024",
			"datedDate": "2023-11-15T00:00:00",
			"accruedInterestPer1000": "8.0906600000",
			"accruedInterestPer100": "",
			"adjustedAccruedInterestPer1000": "",
			"adjustedPrice": "",
			"allocationPercentage": "",
			"allocationPercentageDecimals": "2",
			"announcedCusip": "",
			"auctionFormat": "Single-Price",
			"averageMedianDiscountRate": "",
			"averageMedianInvestmentRate": "",
			"averageMedianPrice": "",
			"averageMedianDiscountMargin": "",
			"averageMedianYield": "",
			"backDated": "Yes",
			"backDatedDate": "2023-11-15T00:00:00",
			"bidToCoverRatio": "",
			"callDate": "",
			"callable": "No",
			"calledDate": "",
			"cashManagementBillCMB": "No",
			"closingTimeCompetitive": "01:00 PM",
			"closingTimeNoncompetitive": "12:00 PM",
			"competitiveAccepted": "",
			"competitiveBidDecimals": "3",
			"competitiveTendered": "",
			"competitiveTendersAccepted": "Yes",
			"corpusCusip": "912803GW7",
			"cpiBaseReferencePeriod": "",
			"currentlyOutstanding": "45445000000.000000",
			"directBidderAccepted": "",
			"directBidderTendered": "",
			"estimatedAmountOfPubliclyHeldMaturingSecuritiesByType": "91910000000",
			"fimaIncluded": "Yes",
			"fimaNoncompetitiveAccepted": "",
			"fimaNoncompetitiveTendered": "",
			"firstInterestPeriod": "Normal",
			"firstInterestPaymentDate": "2024-05-15T00:00:00",
			"floatingRate": "No",
			"frnIndexDeterminationDate": "",
			"frnIndexDeterminationRate": "",
			"highDiscountRate": "",
			"highInvestmentRate": "",
			"highPrice": "",
			"highDiscountMargin": "",
			"highYield": "",
			"indexRatioOnIssueDate": "",
			"indirectBidderAccepted": "",
			"indirectBidderTendered": "",
			"interestPaymentFrequency": "Semi-Annual",
			"lowDiscountRate": "",
			"lowInvestmentRate": "",
			"lowPrice": "",
			"lowDiscountMargin": "",
			"lowYield": "",
			"maturingDate": "2024-01-15T00:00:00",
			"maximumCompetitiveAward": "7350000000",
			"maximumNoncompetitiveAward": "10000000",
			"maximumSingleBid": "7350000000",
			"minimumBidAmount": "100",
			"minimumStripAmount": "100",
			"minimumToIssue": "100",
			"multiplesToBid": "100",
			"multiplesToIssue": "100",
			"nlpExclusionAmount": "15800000000",
			"nlpReportingThreshold": "7350000000",
			"noncompetitiveAccepted": "",
			"noncompetitiveTendersAccepted": "Yes",
			"offeringAmount": "21000000000",
			"originalCusip": "",
			"originalDatedDate": "2023-11-15T00:00:00",
			"originalIssueDate": "2023-11-15T00:00:00",
			"originalSecurityTerm": "30-Year",
			"pdfFilenameAnnouncement": "A_20240104_4.pdf",
			"pdfFilenameCompetitiveResults": "",
			"pdfFilenameNoncompetitiveResults": "",
			"pdfFilenameSpecialAnnouncement": "",
			"pricePer100": "",
			"primaryDealerAccepted": "",
			"primaryDealerTendered": "",
			"reopening": "Yes",
			"securityTermDayMonth": "10-Month",
			"securityTermWeekYear": "29-Year",
			"series": "Bonds of November 2053",
			"somaAccepted": "",
			"somaHoldings": "25907000000",
			"somaIncluded": "No",
			"somaTendered": "",
			"spread": "",
			"standardInterestPaymentPer1000": "23.7500",
			"strippable": "Yes",
			"term": "30-Year",
			"tiinConversionFactorPer1000": "",
			"tips": "No",
			"totalAccepted": "",
			"totalTendered": "",
			"treasuryRetailAccepted": "",
			"treasuryRetailTendersAccepted": "Yes",
			"type": "Bond",
			"unadjustedAccruedInterestPer1000": "",
			"unadjustedPrice": "",
			"updatedTimestamp": "2024-01-04T11:02:28",
			"xmlFilenameAnnouncement": "A_20240104_4.xml",
			"xmlFilenameCompetitiveResults": "",
			"xmlFilenameSpecialAnnouncement": "",
			"tintCusip1": "",
			"tintCusip2": ""
		},
		{
			"cusip": "912810TV0",
			"issueDate": "2023-12-15T00:00:00",
			"securityType": "Bond",
			"securityTerm": "29-Year 11-Month",
			"maturityDate": "2053-11-15T00:00:00",
			"interestRate": "4.750000",
			"refCpiOnIssueDate": "",
			"refCpiOnDatedDate": "",
			"announcementDate": "2023-12-07T00:00:00",
			"auctionDate": "2023-12-12T00:00:00",
			"auctionDateYear": "2023",
			"datedDate": "2023-11-15T00:00:00",
			"accruedInterestPer1000": "3.9148400000",
			"accruedInterestPer100": "",
			"adjustedAccruedInterestPer1000": "",
			"adjustedPrice": "",
			"allocationPercentage": "93.570000",
			"allocationPercentageDecimals": "2",
			"announcedCusip": "",
			"auctionFormat": "Single-Price",
			"averageMedianDiscountRate": "",
			"averageMedianInvestmentRate": "",
			"averageMedianPrice": "",
			"averageMedianDiscountMargin": "",
			"averageMedianYield": "4.280000",
			"backDated": "Yes",
			"backDatedDate": "2023-11-15T00:00:00",
			"bidToCoverRatio": "2.430000",
			"callDate": "",
			"callable": "No",
			"calledDate": "",
			"cashManagementBillCMB": "No",
			"closingTimeCompetitive": "01:00 PM",
			"closingTimeNoncompetitive": "12:00 PM",
			"competitiveAccepted": "20933494500",
			"competitiveBidDecimals": "3",
			"competitiveTendered": "50944732000",
			"competitiveTendersAccepted": "Yes",
			"corpusCusip": "912803GW7",
			"cpiBaseReferencePeriod": "",
			"currentlyOutstanding": "24457000000.000000",
			"directBidderAccepted": "3621800000",
			"directBidderTendered": "6565300000",
			"estimatedAmountOfPubliclyHeldMaturingSecuritiesByType": "44215000000",
			"fimaIncluded": "Yes",
			"fimaNoncompetitiveAccepted": "0",
			"fimaNoncompetitiveTendered": "0",
			"firstInterestPeriod": "Normal",
			"firstInterestPaymentDate": "2024-05-15T00:00:00",
			"floatingRate": "No",
			"frnIndexDeterminationDate": "",
			"frnIndexDeterminationRate": "",
			"highDiscountRate": "",
			"highInvestmentRate": "",
			"highPrice": "106.755520",
			"highDiscountMargin": "",
			"highYield": "4.3440",
			"indexRatioOnIssueDate": "",
			"indirectBidderAccepted": "14333694500",
			"indirectBidderTendered": "16508432000",
			"interestPaymentFrequency": "Semi-Annual",
			"lowDiscountRate": "",
			"lowInvestmentRate": "",
			"lowPrice": "",
			"lowDiscountMargin": "",
			"lowYield": "4.230000",
			"maturingDate": "2023-12-15T00:00:00",
			"maximumCompetitiveAward": "7350000000",
			"maximumNoncompetitiveAward": "10000000",
			"maximumSingleBid": "7350000000",
			"minimumBidAmount": "100",
			"minimumStripAmount": "100",
			"minimumToIssue": "100",
			"multiplesToBid": "100",
			"multiplesToIssue": "100",
			"nlpExclusionAmount": "8400000000",
			"nlpReportingThreshold": "7350000000",
			"noncompetitiveAccepted": "66507500",
			"noncompetitiveTendersAccepted": "Yes",
			"offeringAmount": "21000000000",
			"originalCusip": "",
			"originalDatedDate": "2023-11-15T00:00:00",
			"originalIssueDate": "2023-11-15T00:00:00",
			"originalSecurityTerm": "30-Year",
			"pdfFilenameAnnouncement": "A_20231207_4.pdf",
			"pdfFilenameCompetitiveResults": "R_20231212_2.pdf",
			"pdfFilenameNoncompetitiveResults": "NCR_20231212_2.pdf",
			"pdfFilenameSpecialAnnouncement": "",
			"pricePer100": "106.755520",
			"primaryDealerAccepted": "2978000000",
			"primaryDealerTendered": "27871000000",
			"reopening": "Yes",
			"securityTermDayMonth": "11-Month",
			"securityTermWeekYear": "29-Year",
			"series": "Bonds of November 2053",
			"somaAccepted": "0",
			"somaHoldings": "14170000000",
			"somaIncluded": "No",
			"somaTendered": "0",
			"spread": "",
			"standardInterestPaymentPer1000": "23.7500",
			"strippable": "Yes",
			"term": "30-Year",
			"tiinConversionFactorPer1000": "",
			"tips": "No",
			"totalAccepted": "21000002000",
			"totalTendered": "51011239500",
			"treasuryRetailAccepted": "24167500",
			"treasuryRetailTendersAccepted": "Yes",
			"type": "Bond",
			"unadjustedAccruedInterestPer1000": "",
			"unadjustedPrice": "",
			"updatedTimestamp": "2023-12-12T13:04:55",
			"xmlFilenameAnnouncement": "A_20231207_4.xml",
			"xmlFilenameCompetitiveResults": "R_20231212_2.xml",
			"xmlFilenameSpecialAnnouncement": "",
			"tintCusip1": "",
			"tintCusip2": ""
	},
		{
			"cusip": "912810TV0",
			"issueDate": "2023-11-15T00:00:00",
			"securityType": "Bond",
			"securityTerm": "30-Year",
			"maturityDate": "2053-11-15T00:00:00",
			"interestRate": "4.750000",
			"refCpiOnIssueDate": "",
			"refCpiOnDatedDate": "",
			"announcementDate": "2023-11-01T00:00:00",
			"auctionDate": "2023-11-09T00:00:00",
			"auctionDateYear": "2023",
			"datedDate": "2023-11-15T00:00:00",
			"accruedInterestPer1000": "",
			"accruedInterestPer100": "",
			"adjustedAccruedInterestPer1000": "",
			"adjustedPrice": "",
			"allocationPercentage": "17.970000",
			"allocationPercentageDecimals": "2",
			"announcedCusip": "",
			"auctionFormat": "Single-Price",
			"averageMedianDiscountRate": "",
			"averageMedianInvestmentRate": "",
			"averageMedianPrice": "",
			"averageMedianDiscountMargin": "",
			"averageMedianYield": "4.650000",
			"backDated": "No",
			"backDatedDate": "",
			"bidToCoverRatio": "2.240000",
			"callDate": "",
			"callable": "No",
			"calledDate": "",
			"cashManagementBillCMB": "No",
			"closingTimeCompetitive": "01:00 PM",
			"closingTimeNoncompetitive": "12:00 PM",
			"competitiveAccepted": "23910420000",
			"competitiveBidDecimals": "3",
			"competitiveTendered": "53578480000",
			"competitiveTendersAccepted": "Yes",
			"corpusCusip": "912803GW7",
			"cpiBaseReferencePeriod": "",
			"currentlyOutstanding": "",
			"directBidderAccepted": "3625500000",
			"directBidderTendered": "6910500000",
			"estimatedAmountOfPubliclyHeldMaturingSecuritiesByType": "102174000000",
			"fimaIncluded": "Yes",
			"fimaNoncompetitiveAccepted": "0",
			"fimaNoncompetitiveTendered": "0",
			"firstInterestPeriod": "Normal",
			"firstInterestPaymentDate": "2024-05-15T00:00:00",
			"floatingRate": "No",
			"frnIndexDeterminationDate": "",
			"frnIndexDeterminationRate": "",
			"highDiscountRate": "",
			"highInvestmentRate": "",
			"highPrice": "99.698482",
			"highDiscountMargin": "",
			"highYield": "4.7690",
			"indexRatioOnIssueDate": "",
			"indirectBidderAccepted": "14371980000",
			"indirectBidderTendered": "15630980000",
			"interestPaymentFrequency": "Semi-Annual",
			"lowDiscountRate": "",
			"lowInvestmentRate": "",
			"lowPrice": "",
			"lowDiscountMargin": "",
			"lowYield": "4.590000",
			"maturingDate": "2023-11-15T00:00:00",
			"maximumCompetitiveAward": "8400000000",
			"maximumNoncompetitiveAward": "10000000",
			"maximumSingleBid": "8400000000",
			"minimumBidAmount": "100",
			"minimumStripAmount": "100",
			"minimumToIssue": "100",
			"multiplesToBid": "100",
			"multiplesToIssue": "100",
			"nlpExclusionAmount": "0",
			"nlpReportingThreshold": "8400000000",
			"noncompetitiveAccepted": "89597100",
			"noncompetitiveTendersAccepted": "Yes",
			"offeringAmount": "24000000000",
			"originalCusip": "",
			"originalDatedDate": "",
			"originalIssueDate": "",
			"originalSecurityTerm": "30-Year",
			"pdfFilenameAnnouncement": "A_20231101_3.pdf",
			"pdfFilenameCompetitiveResults": "R_20231109_3.pdf",
			"pdfFilenameNoncompetitiveResults": "NCR_20231109_3.pdf",
			"pdfFilenameSpecialAnnouncement": "",
			"pricePer100": "99.698482",
			"primaryDealerAccepted": "5912940000",
			"primaryDealerTendered": "31037000000",
			"reopening": "No",
			"securityTermDayMonth": "0-Month",
			"securityTermWeekYear": "30-Year",
			"series": "Bonds of November 2053",
			"somaAccepted": "456715300",
			"somaHoldings": "32629000000",
			"somaIncluded": "No",
			"somaTendered": "456715300",
			"spread": "",
			"standardInterestPaymentPer1000": "23.7500",
			"strippable": "Yes",
			"term": "30-Year",
			"tiinConversionFactorPer1000": "",
			"tips": "No",
			"totalAccepted": "24456732400",
			"totalTendered": "54124792400",
			"treasuryRetailAccepted": "22593100",
			"treasuryRetailTendersAccepted": "Yes",
			"type": "Bond",
			"unadjustedAccruedInterestPer1000": "",
			"unadjustedPrice": "",
			"updatedTimestamp": "2023-11-09T13:03:15",
			"xmlFilenameAnnouncement": "A_20231101_3.xml",
			"xmlFilenameCompetitiveResults": "R_20231109_3.xml",
			"xmlFilenameSpecialAnnouncement": "",
			"tintCusip1": "912834J66",
			"tintCusip2": ""
		}
	]

	return mo
