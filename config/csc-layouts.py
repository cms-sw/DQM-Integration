def csclayout(i, p, *rows): i["CSC/Layouts/" + p] = DQMItem(layout=rows)

csclayout(dqmitems,"EMU - CSCs with Format Errors",
["EMU/h2_EMU_CSC_Data_Format_Errors"]
)

csclayout(dqmitems,"EMU - DDU Event Size",
["EMU/h2_EMU_All_DDUs_Event_Size"],
["EMU/hp_EMU_All_DDUs_Average_Event_Size"]
)

csclayout(dqmitems,"EMU - DDU Format Errors",
["EMU/h2_EMU_All_DDUs_Format_Errors"]
)

csclayout(dqmitems,"EMU - DDU Inputs in ERROR/WARNING State",
["EMU/h2_EMU_All_DDUs_Inputs_Errors"],
["EMU/h2_EMU_All_DDUs_Inputs_Warnings"]
)

csclayout(dqmitems,"EMU - DDU Inputs with Data",
["EMU/h2_EMU_All_DDUs_Inputs_with_Data"],
["EMU/hp_EMU_All_DDUs_Average_Inputs_with_Data"]
)

csclayout(dqmitems,"EMU - DDU Live Inputs",
["EMU/h2_EMU_All_DDUs_Live_Inputs"],
["EMU/hp_EMU_All_DDUs_Average_Live_Inputs"]
)

csclayout(dqmitems,"EMU - DDU Reported Errors",
["EMU/h2_EMU_All_DDUs_Trailer_Errors"]
)

csclayout(dqmitems,"EMU - DDUs in Readout",
["EMU/h1_EMU_All_DDUs_in_Readout"],
["EMU/h2_EMU_All_DDUs_L1A_Increment"]
)

csclayout(dqmitems,"EMU - DMBs with Format Errors",
["EMU/h2_EMU_CSC_Format_Errors"]
)

csclayout(dqmitems,"EMU - Data Format Errors and Warnings in Tables",
["EMU/h2_EMU_Readout_Errors",
"EMU/h2_EMU_BinaryChecker_Errors",
"EMU/h2_EMU_BinaryChecker_Warnings"]
)

csclayout(dqmitems,"EMU - Readout Buffer Errors",
["EMU/h2_EMU_All_Readout_Errors"]
)

csclayout(dqmitems,"EMU - Unpacked CSCs",
["EMU/h2_EMU_CSC_Mapped_Unpacked"]
)

csclayout(dqmitems,"EMU - Unpacked DMBs",
["EMU/h2_EMU_CSC_Unpacked"]
)

