def csclayout(i, p, *rows): i["Layouts/CSC Layouts/" + p] = DQMItem(layout=rows)
  
  csclayout(dqmitems,"EMU00 Summary/EMU Test00 - Readout Buffer Errors",
      ["CSC/All_Readout_Errors"]
    )
    csclayout(dqmitems,"EMU00 Summary/EMU Test01 - DDUs in Readout",
      ["CSC/All_DDUs_in_Readout"],
      ["CSC/All_DDUs_L1A_Increment"]
    )
    csclayout(dqmitems,"EMU00 Summary/EMU Test02 - DDU Event Size",
      ["CSC/All_DDUs_Event_Size"],
      ["CSC/All_DDUs_Average_Event_Size"]
    )
    csclayout(dqmitems,"EMU00 Summary/EMU Test03 - DDU Reported Errors",
      ["CSC/All_DDUs_Trailer_Errors"]
    )
    csclayout(dqmitems,"EMU00 Summary/EMU Test04 - DDU Format Errors",
      ["CSC/All_DDUs_Format_Errors"]
    )
    csclayout(dqmitems,"EMU00 Summary/EMU Test05 - DDU Inputs Status",
      ["CSC/All_DDUs_Live_Inputs"],
      ["CSC/All_DDUs_Inputs_with_Data"]
    )
    csclayout(dqmitems,"EMU00 Summary/EMU Test06 - DDU Inputs in ERROR/WARNING State",
      ["CSC/All_DDUs_Inputs_Errors"],
      ["CSC/All_DDUs_Inputs_Warnings"]
    )
    csclayout(dqmitems,"EMU00 Summary/EMU Test08 - CSCs Reporting Data and Unpacked",
      ["CSC/CSC_Reporting"],
      ["CSC/CSC_Unpacked_Fract"]
    )
    csclayout(dqmitems,"EMU00 Summary/EMU Test10 - CSCs with Errors and Warnings (Fractions)",
      ["CSC/CSC_Format_Errors_Fract"],
      ["CSC/CSC_Format_Warnings_Fract"],
      ["CSC/CSC_DMB_input_fifo_full_Fract"],
      ["CSC/CSC_DMB_input_timeout_Fract"]
    )
    csclayout(dqmitems,"EMU00 Summary/EMU Test11 - CSCs without Data Blocks",
      ["CSC/CSC_wo_ALCT_Fract"],
      ["CSC/CSC_wo_CLCT_Fract"],
      ["CSC/CSC_wo_CFEB_Fract"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_36/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_36/DMB_Active_Header_Count"],
      ["CSC/DDU_36/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_36/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_35/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_35/DMB_Active_Header_Count"],
      ["CSC/DDU_35/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_35/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_34/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_34/DMB_Active_Header_Count"],
      ["CSC/DDU_34/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_34/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_33/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_33/DMB_Active_Header_Count"],
      ["CSC/DDU_33/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_33/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_32/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_32/DMB_Active_Header_Count"],
      ["CSC/DDU_32/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_32/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_31/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_31/DMB_Active_Header_Count"],
      ["CSC/DDU_31/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_31/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_30/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_30/DMB_Active_Header_Count"],
      ["CSC/DDU_30/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_30/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_29/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_29/DMB_Active_Header_Count"],
      ["CSC/DDU_29/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_29/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_28/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_28/DMB_Active_Header_Count"],
      ["CSC/DDU_28/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_28/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_27/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_27/DMB_Active_Header_Count"],
      ["CSC/DDU_27/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_27/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_26/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_26/DMB_Active_Header_Count"],
      ["CSC/DDU_26/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_26/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_25/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_25/DMB_Active_Header_Count"],
      ["CSC/DDU_25/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_25/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_24/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_24/DMB_Active_Header_Count"],
      ["CSC/DDU_24/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_24/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_23/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_23/DMB_Active_Header_Count"],
      ["CSC/DDU_23/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_23/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_22/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_22/DMB_Active_Header_Count"],
      ["CSC/DDU_22/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_22/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_21/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_21/DMB_Active_Header_Count"],
      ["CSC/DDU_21/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_21/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_20/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_20/DMB_Active_Header_Count"],
      ["CSC/DDU_20/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_20/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_19/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_19/DMB_Active_Header_Count"],
      ["CSC/DDU_19/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_19/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_18/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_18/DMB_Active_Header_Count"],
      ["CSC/DDU_18/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_18/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_17/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_17/DMB_Active_Header_Count"],
      ["CSC/DDU_17/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_17/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_16/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_16/DMB_Active_Header_Count"],
      ["CSC/DDU_16/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_16/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_15/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_15/DMB_Active_Header_Count"],
      ["CSC/DDU_15/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_15/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_14/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_14/DMB_Active_Header_Count"],
      ["CSC/DDU_14/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_14/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_13/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_13/DMB_Active_Header_Count"],
      ["CSC/DDU_13/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_13/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_12/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_12/DMB_Active_Header_Count"],
      ["CSC/DDU_12/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_12/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_11/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_11/DMB_Active_Header_Count"],
      ["CSC/DDU_11/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_11/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_10/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_10/DMB_Active_Header_Count"],
      ["CSC/DDU_10/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_10/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_09/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_09/DMB_Active_Header_Count"],
      ["CSC/DDU_09/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_09/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_08/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_08/DMB_Active_Header_Count"],
      ["CSC/DDU_08/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_08/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_07/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_07/DMB_Active_Header_Count"],
      ["CSC/DDU_07/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_07/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_06/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_06/DMB_Active_Header_Count"],
      ["CSC/DDU_06/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_06/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_05/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_05/DMB_Active_Header_Count"],
      ["CSC/DDU_05/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_05/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_04/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_04/DMB_Active_Header_Count"],
      ["CSC/DDU_04/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_04/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_03/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_03/DMB_Active_Header_Count"],
      ["CSC/DDU_03/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_03/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_02/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_02/DMB_Active_Header_Count"],
      ["CSC/DDU_02/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_02/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_01/DMBs DAV and Unpacked vs DMBs Active",
      ["CSC/DDU_01/DMB_Active_Header_Count"],
      ["CSC/DDU_01/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count"],
      ["CSC/DDU_01/DMB_unpacked_vs_DAV"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_36/Error Status from DDU Trailer",
      ["CSC/DDU_36/Trailer_ErrorStat_Table"],
      ["CSC/DDU_36/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_35/Error Status from DDU Trailer",
      ["CSC/DDU_35/Trailer_ErrorStat_Table"],
      ["CSC/DDU_35/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_34/Error Status from DDU Trailer",
      ["CSC/DDU_34/Trailer_ErrorStat_Table"],
      ["CSC/DDU_34/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_33/Error Status from DDU Trailer",
      ["CSC/DDU_33/Trailer_ErrorStat_Table"],
      ["CSC/DDU_33/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_32/Error Status from DDU Trailer",
      ["CSC/DDU_32/Trailer_ErrorStat_Table"],
      ["CSC/DDU_32/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_31/Error Status from DDU Trailer",
      ["CSC/DDU_31/Trailer_ErrorStat_Table"],
      ["CSC/DDU_31/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_30/Error Status from DDU Trailer",
      ["CSC/DDU_30/Trailer_ErrorStat_Table"],
      ["CSC/DDU_30/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_29/Error Status from DDU Trailer",
      ["CSC/DDU_29/Trailer_ErrorStat_Table"],
      ["CSC/DDU_29/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_28/Error Status from DDU Trailer",
      ["CSC/DDU_28/Trailer_ErrorStat_Table"],
      ["CSC/DDU_28/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_27/Error Status from DDU Trailer",
      ["CSC/DDU_27/Trailer_ErrorStat_Table"],
      ["CSC/DDU_27/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_26/Error Status from DDU Trailer",
      ["CSC/DDU_26/Trailer_ErrorStat_Table"],
      ["CSC/DDU_26/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_25/Error Status from DDU Trailer",
      ["CSC/DDU_25/Trailer_ErrorStat_Table"],
      ["CSC/DDU_25/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_24/Error Status from DDU Trailer",
      ["CSC/DDU_24/Trailer_ErrorStat_Table"],
      ["CSC/DDU_24/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_23/Error Status from DDU Trailer",
      ["CSC/DDU_23/Trailer_ErrorStat_Table"],
      ["CSC/DDU_23/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_22/Error Status from DDU Trailer",
      ["CSC/DDU_22/Trailer_ErrorStat_Table"],
      ["CSC/DDU_22/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_21/Error Status from DDU Trailer",
      ["CSC/DDU_21/Trailer_ErrorStat_Table"],
      ["CSC/DDU_21/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_20/Error Status from DDU Trailer",
      ["CSC/DDU_20/Trailer_ErrorStat_Table"],
      ["CSC/DDU_20/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_19/Error Status from DDU Trailer",
      ["CSC/DDU_19/Trailer_ErrorStat_Table"],
      ["CSC/DDU_19/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_18/Error Status from DDU Trailer",
      ["CSC/DDU_18/Trailer_ErrorStat_Table"],
      ["CSC/DDU_18/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_17/Error Status from DDU Trailer",
      ["CSC/DDU_17/Trailer_ErrorStat_Table"],
      ["CSC/DDU_17/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_16/Error Status from DDU Trailer",
      ["CSC/DDU_16/Trailer_ErrorStat_Table"],
      ["CSC/DDU_16/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_15/Error Status from DDU Trailer",
      ["CSC/DDU_15/Trailer_ErrorStat_Table"],
      ["CSC/DDU_15/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_14/Error Status from DDU Trailer",
      ["CSC/DDU_14/Trailer_ErrorStat_Table"],
      ["CSC/DDU_14/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_13/Error Status from DDU Trailer",
      ["CSC/DDU_13/Trailer_ErrorStat_Table"],
      ["CSC/DDU_13/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_12/Error Status from DDU Trailer",
      ["CSC/DDU_12/Trailer_ErrorStat_Table"],
      ["CSC/DDU_12/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_11/Error Status from DDU Trailer",
      ["CSC/DDU_11/Trailer_ErrorStat_Table"],
      ["CSC/DDU_11/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_10/Error Status from DDU Trailer",
      ["CSC/DDU_10/Trailer_ErrorStat_Table"],
      ["CSC/DDU_10/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_09/Error Status from DDU Trailer",
      ["CSC/DDU_09/Trailer_ErrorStat_Table"],
      ["CSC/DDU_09/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_08/Error Status from DDU Trailer",
      ["CSC/DDU_08/Trailer_ErrorStat_Table"],
      ["CSC/DDU_08/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_07/Error Status from DDU Trailer",
      ["CSC/DDU_07/Trailer_ErrorStat_Table"],
      ["CSC/DDU_07/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_06/Error Status from DDU Trailer",
      ["CSC/DDU_06/Trailer_ErrorStat_Table"],
      ["CSC/DDU_06/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_05/Error Status from DDU Trailer",
      ["CSC/DDU_05/Trailer_ErrorStat_Table"],
      ["CSC/DDU_05/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_04/Error Status from DDU Trailer",
      ["CSC/DDU_04/Trailer_ErrorStat_Table"],
      ["CSC/DDU_04/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_03/Error Status from DDU Trailer",
      ["CSC/DDU_03/Trailer_ErrorStat_Table"],
      ["CSC/DDU_03/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_02/Error Status from DDU Trailer",
      ["CSC/DDU_02/Trailer_ErrorStat_Table"],
      ["CSC/DDU_02/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_01/Error Status from DDU Trailer",
      ["CSC/DDU_01/Trailer_ErrorStat_Table"],
      ["CSC/DDU_01/Trailer_ErrorStat_Frequency"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_36/Connected and Active Inputs",
      ["CSC/DDU_36/DMB_Connected_Inputs"],
      ["CSC/DDU_36/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_35/Connected and Active Inputs",
      ["CSC/DDU_35/DMB_Connected_Inputs"],
      ["CSC/DDU_35/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_34/Connected and Active Inputs",
      ["CSC/DDU_34/DMB_Connected_Inputs"],
      ["CSC/DDU_34/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_33/Connected and Active Inputs",
      ["CSC/DDU_33/DMB_Connected_Inputs"],
      ["CSC/DDU_33/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_32/Connected and Active Inputs",
      ["CSC/DDU_32/DMB_Connected_Inputs"],
      ["CSC/DDU_32/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_31/Connected and Active Inputs",
      ["CSC/DDU_31/DMB_Connected_Inputs"],
      ["CSC/DDU_31/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_30/Connected and Active Inputs",
      ["CSC/DDU_30/DMB_Connected_Inputs"],
      ["CSC/DDU_30/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_29/Connected and Active Inputs",
      ["CSC/DDU_29/DMB_Connected_Inputs"],
      ["CSC/DDU_29/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_28/Connected and Active Inputs",
      ["CSC/DDU_28/DMB_Connected_Inputs"],
      ["CSC/DDU_28/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_27/Connected and Active Inputs",
      ["CSC/DDU_27/DMB_Connected_Inputs"],
      ["CSC/DDU_27/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_26/Connected and Active Inputs",
      ["CSC/DDU_26/DMB_Connected_Inputs"],
      ["CSC/DDU_26/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_25/Connected and Active Inputs",
      ["CSC/DDU_25/DMB_Connected_Inputs"],
      ["CSC/DDU_25/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_24/Connected and Active Inputs",
      ["CSC/DDU_24/DMB_Connected_Inputs"],
      ["CSC/DDU_24/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_23/Connected and Active Inputs",
      ["CSC/DDU_23/DMB_Connected_Inputs"],
      ["CSC/DDU_23/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_22/Connected and Active Inputs",
      ["CSC/DDU_22/DMB_Connected_Inputs"],
      ["CSC/DDU_22/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_21/Connected and Active Inputs",
      ["CSC/DDU_21/DMB_Connected_Inputs"],
      ["CSC/DDU_21/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_20/Connected and Active Inputs",
      ["CSC/DDU_20/DMB_Connected_Inputs"],
      ["CSC/DDU_20/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_19/Connected and Active Inputs",
      ["CSC/DDU_19/DMB_Connected_Inputs"],
      ["CSC/DDU_19/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_18/Connected and Active Inputs",
      ["CSC/DDU_18/DMB_Connected_Inputs"],
      ["CSC/DDU_18/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_17/Connected and Active Inputs",
      ["CSC/DDU_17/DMB_Connected_Inputs"],
      ["CSC/DDU_17/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_16/Connected and Active Inputs",
      ["CSC/DDU_16/DMB_Connected_Inputs"],
      ["CSC/DDU_16/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_15/Connected and Active Inputs",
      ["CSC/DDU_15/DMB_Connected_Inputs"],
      ["CSC/DDU_15/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_14/Connected and Active Inputs",
      ["CSC/DDU_14/DMB_Connected_Inputs"],
      ["CSC/DDU_14/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_13/Connected and Active Inputs",
      ["CSC/DDU_13/DMB_Connected_Inputs"],
      ["CSC/DDU_13/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_12/Connected and Active Inputs",
      ["CSC/DDU_12/DMB_Connected_Inputs"],
      ["CSC/DDU_12/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_11/Connected and Active Inputs",
      ["CSC/DDU_11/DMB_Connected_Inputs"],
      ["CSC/DDU_11/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_10/Connected and Active Inputs",
      ["CSC/DDU_10/DMB_Connected_Inputs"],
      ["CSC/DDU_10/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_09/Connected and Active Inputs",
      ["CSC/DDU_09/DMB_Connected_Inputs"],
      ["CSC/DDU_09/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_08/Connected and Active Inputs",
      ["CSC/DDU_08/DMB_Connected_Inputs"],
      ["CSC/DDU_08/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_07/Connected and Active Inputs",
      ["CSC/DDU_07/DMB_Connected_Inputs"],
      ["CSC/DDU_07/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_06/Connected and Active Inputs",
      ["CSC/DDU_06/DMB_Connected_Inputs"],
      ["CSC/DDU_06/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_05/Connected and Active Inputs",
      ["CSC/DDU_05/DMB_Connected_Inputs"],
      ["CSC/DDU_05/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_04/Connected and Active Inputs",
      ["CSC/DDU_04/DMB_Connected_Inputs"],
      ["CSC/DDU_04/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_03/Connected and Active Inputs",
      ["CSC/DDU_03/DMB_Connected_Inputs"],
      ["CSC/DDU_03/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_02/Connected and Active Inputs",
      ["CSC/DDU_02/DMB_Connected_Inputs"],
      ["CSC/DDU_02/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_01/Connected and Active Inputs",
      ["CSC/DDU_01/DMB_Connected_Inputs"],
      ["CSC/DDU_01/DMB_DAV_Header_Occupancy"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_36/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_36/Buffer_Size"],
      ["CSC/DDU_36/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_35/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_35/Buffer_Size"],
      ["CSC/DDU_35/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_34/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_34/Buffer_Size"],
      ["CSC/DDU_34/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_33/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_33/Buffer_Size"],
      ["CSC/DDU_33/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_32/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_32/Buffer_Size"],
      ["CSC/DDU_32/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_31/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_31/Buffer_Size"],
      ["CSC/DDU_31/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_30/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_30/Buffer_Size"],
      ["CSC/DDU_30/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_29/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_29/Buffer_Size"],
      ["CSC/DDU_29/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_28/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_28/Buffer_Size"],
      ["CSC/DDU_28/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_27/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_27/Buffer_Size"],
      ["CSC/DDU_27/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_26/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_26/Buffer_Size"],
      ["CSC/DDU_26/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_25/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_25/Buffer_Size"],
      ["CSC/DDU_25/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_24/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_24/Buffer_Size"],
      ["CSC/DDU_24/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_23/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_23/Buffer_Size"],
      ["CSC/DDU_23/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_22/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_22/Buffer_Size"],
      ["CSC/DDU_22/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_21/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_21/Buffer_Size"],
      ["CSC/DDU_21/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_20/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_20/Buffer_Size"],
      ["CSC/DDU_20/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_19/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_19/Buffer_Size"],
      ["CSC/DDU_19/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_18/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_18/Buffer_Size"],
      ["CSC/DDU_18/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_17/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_17/Buffer_Size"],
      ["CSC/DDU_17/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_16/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_16/Buffer_Size"],
      ["CSC/DDU_16/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_15/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_15/Buffer_Size"],
      ["CSC/DDU_15/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_14/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_14/Buffer_Size"],
      ["CSC/DDU_14/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_13/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_13/Buffer_Size"],
      ["CSC/DDU_13/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_12/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_12/Buffer_Size"],
      ["CSC/DDU_12/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_11/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_11/Buffer_Size"],
      ["CSC/DDU_11/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_10/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_10/Buffer_Size"],
      ["CSC/DDU_10/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_09/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_09/Buffer_Size"],
      ["CSC/DDU_09/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_08/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_08/Buffer_Size"],
      ["CSC/DDU_08/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_07/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_07/Buffer_Size"],
      ["CSC/DDU_07/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_06/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_06/Buffer_Size"],
      ["CSC/DDU_06/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_05/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_05/Buffer_Size"],
      ["CSC/DDU_05/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_04/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_04/Buffer_Size"],
      ["CSC/DDU_04/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_03/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_03/Buffer_Size"],
      ["CSC/DDU_03/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_02/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_02/Buffer_Size"],
      ["CSC/DDU_02/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_01/Event Buffer Size and DDU Word Count",
      ["CSC/DDU_01/Buffer_Size"],
      ["CSC/DDU_01/Word_Count"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_36/L1A and BXN Counters",
      ["CSC/DDU_36/BXN"],
      ["CSC/DDU_36/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_35/L1A and BXN Counters",
      ["CSC/DDU_35/BXN"],
      ["CSC/DDU_35/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_34/L1A and BXN Counters",
      ["CSC/DDU_34/BXN"],
      ["CSC/DDU_34/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_33/L1A and BXN Counters",
      ["CSC/DDU_33/BXN"],
      ["CSC/DDU_33/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_32/L1A and BXN Counters",
      ["CSC/DDU_32/BXN"],
      ["CSC/DDU_32/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_31/L1A and BXN Counters",
      ["CSC/DDU_31/BXN"],
      ["CSC/DDU_31/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_30/L1A and BXN Counters",
      ["CSC/DDU_30/BXN"],
      ["CSC/DDU_30/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_29/L1A and BXN Counters",
      ["CSC/DDU_29/BXN"],
      ["CSC/DDU_29/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_28/L1A and BXN Counters",
      ["CSC/DDU_28/BXN"],
      ["CSC/DDU_28/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_27/L1A and BXN Counters",
      ["CSC/DDU_27/BXN"],
      ["CSC/DDU_27/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_26/L1A and BXN Counters",
      ["CSC/DDU_26/BXN"],
      ["CSC/DDU_26/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_25/L1A and BXN Counters",
      ["CSC/DDU_25/BXN"],
      ["CSC/DDU_25/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_24/L1A and BXN Counters",
      ["CSC/DDU_24/BXN"],
      ["CSC/DDU_24/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_23/L1A and BXN Counters",
      ["CSC/DDU_23/BXN"],
      ["CSC/DDU_23/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_22/L1A and BXN Counters",
      ["CSC/DDU_22/BXN"],
      ["CSC/DDU_22/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_21/L1A and BXN Counters",
      ["CSC/DDU_21/BXN"],
      ["CSC/DDU_21/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_20/L1A and BXN Counters",
      ["CSC/DDU_20/BXN"],
      ["CSC/DDU_20/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_19/L1A and BXN Counters",
      ["CSC/DDU_19/BXN"],
      ["CSC/DDU_19/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_18/L1A and BXN Counters",
      ["CSC/DDU_18/BXN"],
      ["CSC/DDU_18/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_17/L1A and BXN Counters",
      ["CSC/DDU_17/BXN"],
      ["CSC/DDU_17/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_16/L1A and BXN Counters",
      ["CSC/DDU_16/BXN"],
      ["CSC/DDU_16/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_15/L1A and BXN Counters",
      ["CSC/DDU_15/BXN"],
      ["CSC/DDU_15/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_14/L1A and BXN Counters",
      ["CSC/DDU_14/BXN"],
      ["CSC/DDU_14/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_13/L1A and BXN Counters",
      ["CSC/DDU_13/BXN"],
      ["CSC/DDU_13/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_12/L1A and BXN Counters",
      ["CSC/DDU_12/BXN"],
      ["CSC/DDU_12/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_11/L1A and BXN Counters",
      ["CSC/DDU_11/BXN"],
      ["CSC/DDU_11/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_10/L1A and BXN Counters",
      ["CSC/DDU_10/BXN"],
      ["CSC/DDU_10/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_09/L1A and BXN Counters",
      ["CSC/DDU_09/BXN"],
      ["CSC/DDU_09/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_08/L1A and BXN Counters",
      ["CSC/DDU_08/BXN"],
      ["CSC/DDU_08/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_07/L1A and BXN Counters",
      ["CSC/DDU_07/BXN"],
      ["CSC/DDU_07/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_06/L1A and BXN Counters",
      ["CSC/DDU_06/BXN"],
      ["CSC/DDU_06/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_05/L1A and BXN Counters",
      ["CSC/DDU_05/BXN"],
      ["CSC/DDU_05/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_04/L1A and BXN Counters",
      ["CSC/DDU_04/BXN"],
      ["CSC/DDU_04/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_03/L1A and BXN Counters",
      ["CSC/DDU_03/BXN"],
      ["CSC/DDU_03/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_02/L1A and BXN Counters",
      ["CSC/DDU_02/BXN"],
      ["CSC/DDU_02/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_01/L1A and BXN Counters",
      ["CSC/DDU_01/BXN"],
      ["CSC/DDU_01/L1A_Increment"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_36/State of CSCs",
      ["CSC/DDU_36/CSC_Errors"],
      ["CSC/DDU_36/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_35/State of CSCs",
      ["CSC/DDU_35/CSC_Errors"],
      ["CSC/DDU_35/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_34/State of CSCs",
      ["CSC/DDU_34/CSC_Errors"],
      ["CSC/DDU_34/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_33/State of CSCs",
      ["CSC/DDU_33/CSC_Errors"],
      ["CSC/DDU_33/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_32/State of CSCs",
      ["CSC/DDU_32/CSC_Errors"],
      ["CSC/DDU_32/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_31/State of CSCs",
      ["CSC/DDU_31/CSC_Errors"],
      ["CSC/DDU_31/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_30/State of CSCs",
      ["CSC/DDU_30/CSC_Errors"],
      ["CSC/DDU_30/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_29/State of CSCs",
      ["CSC/DDU_29/CSC_Errors"],
      ["CSC/DDU_29/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_28/State of CSCs",
      ["CSC/DDU_28/CSC_Errors"],
      ["CSC/DDU_28/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_27/State of CSCs",
      ["CSC/DDU_27/CSC_Errors"],
      ["CSC/DDU_27/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_26/State of CSCs",
      ["CSC/DDU_26/CSC_Errors"],
      ["CSC/DDU_26/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_25/State of CSCs",
      ["CSC/DDU_25/CSC_Errors"],
      ["CSC/DDU_25/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_24/State of CSCs",
      ["CSC/DDU_24/CSC_Errors"],
      ["CSC/DDU_24/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_23/State of CSCs",
      ["CSC/DDU_23/CSC_Errors"],
      ["CSC/DDU_23/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_22/State of CSCs",
      ["CSC/DDU_22/CSC_Errors"],
      ["CSC/DDU_22/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_21/State of CSCs",
      ["CSC/DDU_21/CSC_Errors"],
      ["CSC/DDU_21/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_20/State of CSCs",
      ["CSC/DDU_20/CSC_Errors"],
      ["CSC/DDU_20/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_19/State of CSCs",
      ["CSC/DDU_19/CSC_Errors"],
      ["CSC/DDU_19/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_18/State of CSCs",
      ["CSC/DDU_18/CSC_Errors"],
      ["CSC/DDU_18/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_17/State of CSCs",
      ["CSC/DDU_17/CSC_Errors"],
      ["CSC/DDU_17/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_16/State of CSCs",
      ["CSC/DDU_16/CSC_Errors"],
      ["CSC/DDU_16/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_15/State of CSCs",
      ["CSC/DDU_15/CSC_Errors"],
      ["CSC/DDU_15/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_14/State of CSCs",
      ["CSC/DDU_14/CSC_Errors"],
      ["CSC/DDU_14/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_13/State of CSCs",
      ["CSC/DDU_13/CSC_Errors"],
      ["CSC/DDU_13/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_12/State of CSCs",
      ["CSC/DDU_12/CSC_Errors"],
      ["CSC/DDU_12/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_11/State of CSCs",
      ["CSC/DDU_11/CSC_Errors"],
      ["CSC/DDU_11/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_10/State of CSCs",
      ["CSC/DDU_10/CSC_Errors"],
      ["CSC/DDU_10/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_09/State of CSCs",
      ["CSC/DDU_09/CSC_Errors"],
      ["CSC/DDU_09/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_08/State of CSCs",
      ["CSC/DDU_08/CSC_Errors"],
      ["CSC/DDU_08/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_07/State of CSCs",
      ["CSC/DDU_07/CSC_Errors"],
      ["CSC/DDU_07/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_06/State of CSCs",
      ["CSC/DDU_06/CSC_Errors"],
      ["CSC/DDU_06/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_05/State of CSCs",
      ["CSC/DDU_05/CSC_Errors"],
      ["CSC/DDU_05/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_04/State of CSCs",
      ["CSC/DDU_04/CSC_Errors"],
      ["CSC/DDU_04/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_03/State of CSCs",
      ["CSC/DDU_03/CSC_Errors"],
      ["CSC/DDU_03/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_02/State of CSCs",
      ["CSC/DDU_02/CSC_Errors"],
      ["CSC/DDU_02/CSC_Warnings"]
    )
    csclayout(dqmitems,"EMU01 DDUs/DDU_01/State of CSCs",
      ["CSC/DDU_01/CSC_Errors"],
      ["CSC/DDU_01/CSC_Warnings"]
    )
    