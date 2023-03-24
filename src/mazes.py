

def maze_gen(input):
    maze_8x8=[
    "###G####-0",
    "#      #-1",
    "# #### #-2",
    "# #    #-3",
    "# # #  #-4",
    "#   #  #-5",
    "### # ##-6",
    "#####S##-7"
    ]

    maze_32x32=[
"###########G####################-0",
"####### # #         ### # # #  #-1",
"#           # # # #       #    #-2",
"# # # # ############# # ##### ##-3",
"# # # # # #     #     #     #  #-4",
"### # # # # # ##### ##### # #  #-5",
"# # # #   # #     # #     # #  #-6",
"# # ######### # ### # # ### #  #-7",
"#     #   # # #     # # # # #  #-8",
"######### # ####### # ### #### #-9",
"#     #       # #   #   #      #10",
"##### # # ### # ### ##### # ## #11",
"#   #   # #       #   #   #    #12",
"# ##### ### # ### ### ##### # ##13",
"#   #   #   #   #     #     #  #14",
"# # ##### ####### # ########## #15",
"# #       #   # # #            #16",
"######### # ### ##### # #####  #17",
"#     #   #   # #   # # # #    #18",
"# ### ##### ### ### # ### # #  #19",
"#   # #         #         # #  #20",
"# # ##### ### ### # ####### ## #21",
"# # #       #   # # # #     #  #22",
"# ##### ##### # ### # # # ######23",
"#   #   #   # #     # # # #    #24",
"# ### # # ### # ### # ######## #25",
"#   # #   # # #   #     #   #  #26",
"# ### ##### # ########### # #  #27",
"#         # # #           #    #28",
"# # ### # # # ### # ##### #### #29",
"# #   # # #       #   #     #  #30",
"#############################S##31" 
    ]
    if input==0:
        return maze_8x8
    else:
        return maze_32x32

for i in maze_gen(1):
    print(i)