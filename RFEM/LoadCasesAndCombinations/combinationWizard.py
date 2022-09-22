from RFEM.initModel import Model, clearAtributes

class CombinationWizard():

    def __init__(self,
                 comment: str = '',
                 params: dict = {
                    "current_standard_for_combination_wizard": 6207,
                    "activate_combination_wizard_and_classification": True,
                    "activate_combination_wizard": True,
                    "result_combinations_active": False,
                    "result_combinations_parentheses_active": False,
                    "result_combinations_consider_sub_results": False,
                    "combination_name_according_to_action_category": False
                 },
                 model= Model):

        """
        Args:
            comment(str, optional): Comments
            params(dict, optional): Combination Wizard Parameters

                        National Annex                                      Codes
                       ----------------                                     -----
        NATIONAL_ANNEX_AND_EDITION_EN_1990_CEN_2010_04		                6207
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BDS_2015_02		                6034
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BS_2009_06		                6035
        NATIONAL_ANNEX_AND_EDITION_EN_1990_CSN_2015_05		                6036
        NATIONAL_ANNEX_AND_EDITION_EN_1990_CYS_2010_06		                6037
        NATIONAL_ANNEX_AND_EDITION_EN_1990_DIN_2012_08		                6038
        NATIONAL_ANNEX_AND_EDITION_EN_1990_DS_2013_05		                6039
        NATIONAL_ANNEX_AND_EDITION_EN_1990_ELOT_2009_01		                6360
        NATIONAL_ANNEX_AND_EDITION_EN_1990_EVS_2010_04		                6548
        NATIONAL_ANNEX_AND_EDITION_EN_1990_I_S_2010_03		                6040
        NATIONAL_ANNEX_AND_EDITION_EN_1990_ILNAS_2020_03		            6042
        NATIONAL_ANNEX_AND_EDITION_EN_1990_LST_2012_01		                6041
        NATIONAL_ANNEX_AND_EDITION_EN_1990_LVS_2015_01		                6043
        NATIONAL_ANNEX_AND_EDITION_EN_1990_MS_2010_05		                6044
        NATIONAL_ANNEX_AND_EDITION_EN_1990_NBN_2015_07		                6045
        NATIONAL_ANNEX_AND_EDITION_EN_1990_NEN_2007_09		                6046
        NATIONAL_ANNEX_AND_EDITION_EN_1990_NEN_2019_11		                6047
        NATIONAL_ANNEX_AND_EDITION_EN_1990_NF_2011_12		                6048
        NATIONAL_ANNEX_AND_EDITION_EN_1990_NP_2009_12		                6049
        NATIONAL_ANNEX_AND_EDITION_EN_1990_NS_2016_05		                6050
        NATIONAL_ANNEX_AND_EDITION_EN_1990_OENORM_2013_03		            6051
        NATIONAL_ANNEX_AND_EDITION_EN_1990_PN_2010_09		                6052
        NATIONAL_ANNEX_AND_EDITION_EN_1990_SFS_2010_09		                6053
        NATIONAL_ANNEX_AND_EDITION_EN_1990_SIST_2010_09		                6054
        NATIONAL_ANNEX_AND_EDITION_EN_1990_SR_2009_10		                6055
        NATIONAL_ANNEX_AND_EDITION_EN_1990_SS_2012_06		                6056
        NATIONAL_ANNEX_AND_EDITION_EN_1990_SS_2010_04		                6057
        NATIONAL_ANNEX_AND_EDITION_EN_1990_SS_2019_01		                6414
        NATIONAL_ANNEX_AND_EDITION_EN_1990_STN_2010_11		                6058
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TKP_2011_11		                6059
        NATIONAL_ANNEX_AND_EDITION_EN_1990_UNE_2019_04		                6060
        NATIONAL_ANNEX_AND_EDITION_EN_1990_UNI_2010_10		                6061
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_CEN_2010_04	            6208
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_BDS_2015_02		        6062
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_BS_2009_06		        6063
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_CSN_2015_05		        6064
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_CYS_2010_06		        6065
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_DIN_2012_08		        6066
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_DS_2013_09		        6067
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_I_S_2010_03		        6068
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_ILNAS_2020_03		        6070
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_LST_2012_01		        6069
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_LVS_2015_01		        6071
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_NBN_2015_07		        6072
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_NEN_2007_09		        6073
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_NEN_2019_11		        6074
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_NF_2015_01		        6075
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_NP_2009_12		        6076
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_NS_2016_05		        6077
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_OENORM_2009_07	        6078
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_OENORM_2019_06		    6079
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_PN_2010_09		        6080
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_SFS_2010_09		        6081
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_SIST_2010_09		        6082
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_SR_2009_10		        6083
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_SS_2010_04		        6084
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_SS_2019_01		        6415
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_STN_2010_11		        6085
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_TKP_2011_11		        6351
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_UNE_2010_07		        6086
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_UNE_2019_04		        6087
        NATIONAL_ANNEX_AND_EDITION_EN_1990_TIMBER_UNI_2010_10		        6088
        NATIONAL_ANNEX_AND_EDITION_EN_1990_CRANES_CEN_2010_04		        6209
        NATIONAL_ANNEX_AND_EDITION_EN_1990_CRANES_DIN_2012_08		        6089
        NATIONAL_ANNEX_AND_EDITION_EN_1990_GEOTECHNICS_CEN_2010_04		    6210
        NATIONAL_ANNEX_AND_EDITION_COMBINATION_WIZARD_NONE		            6232
        NATIONAL_ANNEX_AND_EDITION_CAN_CSA_2000		                        6230
        NATIONAL_ANNEX_AND_EDITION_SIA_260_SIA_260_2013_08		            6225
        NATIONAL_ANNEX_AND_EDITION_SIA_260_TIMBER_SIA_260_2013_08		    6226
        NATIONAL_ANNEX_AND_EDITION_CTE_DB_SE_CTE_DB_SE_2009_04		        6227
        NATIONAL_ANNEX_AND_EDITION_ASCE_7_2022_COMBINATION_WIZARD		    6555
        NATIONAL_ANNEX_AND_EDITION_ASCE_7_2016_COMBINATION_WIZARD		    6238
        NATIONAL_ANNEX_AND_EDITION_ASCE_7_2010		                        6237
        NATIONAL_ANNEX_AND_EDITION_ASCE_7_2005		                        6236
        NATIONAL_ANNEX_AND_EDITION_ASCE_7_2002		                        6235
        NATIONAL_ANNEX_AND_EDITION_ASCE_7_WOOD_2022		                    6579
        NATIONAL_ANNEX_AND_EDITION_ASCE_7_WOOD_2016		                    6350
        NATIONAL_ANNEX_AND_EDITION_ASCE_7_WOOD_2010		                    6241
        NATIONAL_ANNEX_AND_EDITION_ASCE_7_WOOD_2005		                    6240
        NATIONAL_ANNEX_AND_EDITION_ASCE_7_WOOD_2002		                    6239
        NATIONAL_ANNEX_AND_EDITION_ACI_318_2019_COMBINATION_WIZARD		    6403
        NATIONAL_ANNEX_AND_EDITION_ACI_318_2014_COMBINATION_WIZARD		    6269
        NATIONAL_ANNEX_AND_EDITION_ACI_318_2011		                        6268
        NATIONAL_ANNEX_AND_EDITION_ACI_318_2008		                        6267
        NATIONAL_ANNEX_AND_EDITION_IBC_2018		                            6361
        NATIONAL_ANNEX_AND_EDITION_IBC_2015		                            6273
        NATIONAL_ANNEX_AND_EDITION_NBC_2015_COMBINATION_WIZARD		        6272
        NATIONAL_ANNEX_AND_EDITION_NBC_2005		                            6271
        NATIONAL_ANNEX_AND_EDITION_NBR_8681_NBR_8681_2003_03		        6270
        NATIONAL_ANNEX_AND_EDITION_IS_800_IS_800_2007_12		            6317
        NATIONAL_ANNEX_AND_EDITION_BS_5950_2000_01		                    6325
        NATIONAL_ANNEX_AND_EDITION_SANS_10160_1_2010_05		                6331
        NATIONAL_ANNEX_AND_EDITION_NBC_WOOD_2015		                    6336
        NATIONAL_ANNEX_AND_EDITION_NTC_NTC_2018_01		                    6358
        NATIONAL_ANNEX_AND_EDITION_SP_20_13330_2016		                    6380
        NATIONAL_ANNEX_AND_EDITION_EN_15512_CEN_2009_03	                    6435
        NATIONAL_ANNEX_AND_EDITION_NTC_TIMBER_2018_01		                6436
        NATIONAL_ANNEX_AND_EDITION_GB_50068_GB_50011_2018		            6514
        NATIONAL_ANNEX_AND_EDITION_GB_50009_GB_50011_2016		            6516
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BASE_TIMBER_CEN_2010_04		    6517
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BASE_TIMBER_BDS_2015_02		    6518
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BASE_TIMBER_BS_2009_06		    6522
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BASE_TIMBER_CSN_2015_05		    6523
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BASE_TIMBER_CYS_2010_06		    6524
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BASE_TIMBER_DIN_2012_08		    6525
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BASE_TIMBER_DS_2013_09		    6526
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BASE_TIMBER_I_S_2010_03		    6527
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BASE_TIMBER_ILNAS_2020_03		6529
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BASE_TIMBER_LST_2012_01		    6528
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BASE_TIMBER_LVS_2015_01		    6530
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BASE_TIMBER_NBN_2015_07		    6531
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BASE_TIMBER_NEN_2019_11		    6532
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BASE_TIMBER_NF_2011_12		    6533
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BASE_TIMBER_NP_2009_12		    6534
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BASE_TIMBER_NS_2016_05		    6535
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BASE_TIMBER_OENORM_2019_06		6536
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BASE_TIMBER_PN_2010_09		    6537
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BASE_TIMBER_SFS_2010_09		    6538
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BASE_TIMBER_SIST_2010_09		    6539
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BASE_TIMBER_SS_2019_01		    6541
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BASE_TIMBER_STN_2010_11		    6521
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BASE_TIMBER_TKP_2011_11		    6542
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BASE_TIMBER_UNE_2019_04		    6543
        NATIONAL_ANNEX_AND_EDITION_EN_1990_BASE_TIMBER_UNI_2010_10		    6544
        NATIONAL_ANNEX_AND_EDITION_AS_NZS_1170_0_2002		                6546
        """

        # Client model | Load Cases And Combinations
        clientObject = model.clientModel.factory.create('ns0:load_cases_and_combinations')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Set Load Case And Combinations to client model
        model.clientModel.service.set_load_cases_and_combinations(clientObject)