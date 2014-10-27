from header_sounds import *

sounds = [
 ("click", sf_2d|sf_vol_3,["drum_3.ogg"]),
 ("tutorial_1", sf_2d|sf_vol_7,["tutorial_1.ogg"]),
 ("tutorial_2", sf_2d|sf_vol_7,["tutorial_2.ogg"]),
 ("gong", sf_2d|sf_priority_9|sf_vol_7, ["Level_earned.wav"]),
 ("quest_taken", sf_2d|sf_priority_9|sf_vol_7, []),
 ("quest_completed", sf_2d|sf_priority_9|sf_vol_8, ["quest_completed.ogg"]),
 ("quest_succeeded", sf_2d|sf_priority_9|sf_vol_6, ["quest_succeeded.ogg"]),
 ("quest_concluded", sf_2d|sf_priority_9|sf_vol_7, ["quest_concluded.ogg"]),
 ("quest_failed", sf_2d|sf_priority_9|sf_vol_7, ["quest_failed.ogg"]),
 ("quest_cancelled", sf_2d|sf_priority_9|sf_vol_7, ["quest_cancelled.ogg"]),
 ("rain",sf_2d|sf_priority_10|sf_vol_4|sf_looping, ["rain_1.ogg"]),
 ("money_received",sf_2d|sf_priority_10|sf_vol_4, ["coins_dropped_1.wav"]),
 ("money_paid",sf_2d|sf_priority_10|sf_vol_10, ["coins_dropped_2.wav"]),
 ("sword_clash_1", sf_priority_5|sf_vol_8,["sword_clank_metal_09.ogg","sword_clank_metal_09b.ogg","sword_clank_metal_10.ogg","sword_clank_metal_10b.ogg","sword_clank_metal_12.ogg","sword_clank_metal_12b.ogg","sword_clank_metal_13.ogg","sword_clank_metal_13b.ogg"]),
 ("sword_clash_2", sf_priority_5|sf_vol_9,["s_swordClash2.wav"]),
 ("sword_clash_3", sf_priority_5|sf_vol_9,["s_swordClash3.wav"]),
 ("sword_swing", sf_vol_8|sf_priority_2,["s_swordSwing.wav"]),
 ("footstep_grass", sf_vol_4|sf_priority_1,["footstep_1.ogg","footstep_2.ogg","footstep_3.ogg","footstep_4.ogg"]),
 ("footstep_wood", sf_vol_5|sf_priority_1,["footstep_wood_1.ogg","footstep_wood_2.ogg","footstep_wood_4.ogg"]),
# ("footstep_wood", sf_vol_3|sf_priority_1,["footstep_stone_1.ogg","footstep_stone_3.ogg","footstep_stone_4.ogg"]),
 ("footstep_water", sf_vol_4|sf_priority_3,["water_walk_1.ogg","water_walk_2.ogg","water_walk_3.ogg","water_walk_4.ogg"]),
 ("footstep_horse",sf_priority_3|sf_vol_8, ["footstep_horse_5.ogg","footstep_horse_2.ogg","footstep_horse_3.ogg","footstep_horse_4.ogg"]),
# ("footstep_horse",0, ["s_footstep_horse_4b.wav","s_footstep_horse_4f.wav","s_footstep_horse_5b.wav","s_footstep_horse_5f.wav"]),
 ("footstep_horse_1b",sf_priority_3|sf_vol_8, ["s_footstep_horse_4b.wav","s_footstep_horse_4f.wav","s_footstep_horse_5b.wav","s_footstep_horse_5f.wav"]),
 ("footstep_horse_1f",sf_priority_3|sf_vol_8, ["s_footstep_horse_2b.wav","s_footstep_horse_2f.wav","s_footstep_horse_3b.wav","s_footstep_horse_3f.wav"]),
# ("footstep_horse_1f",sf_priority_3|sf_vol_8, ["footstep_horse_5.ogg","footstep_horse_2.ogg","footstep_horse_3.ogg","footstep_horse_4.ogg"]),
 ("footstep_horse_2b",sf_priority_3|sf_vol_8, ["s_footstep_horse_2b.wav"]),
 ("footstep_horse_2f",sf_priority_3|sf_vol_8, ["s_footstep_horse_2f.wav"]),
 ("footstep_horse_3b",sf_priority_3|sf_vol_8, ["s_footstep_horse_3b.wav"]),
 ("footstep_horse_3f",sf_priority_3|sf_vol_8, ["s_footstep_horse_3f.wav"]),
 ("footstep_horse_4b",sf_priority_3|sf_vol_8, ["s_footstep_horse_4b.wav"]),
 ("footstep_horse_4f",sf_priority_3|sf_vol_8, ["s_footstep_horse_4f.wav"]),
 ("footstep_horse_5b",sf_priority_3|sf_vol_8, ["s_footstep_horse_5b.wav"]),
 ("footstep_horse_5f",sf_priority_3|sf_vol_8, ["s_footstep_horse_5f.wav"]),
 ("jump_begin", sf_vol_6|sf_priority_9,["jump_begin.ogg"]),
 ("jump_end", sf_vol_5|sf_priority_9,["jump_end.ogg"]),
 ("jump_begin_water", sf_vol_3|sf_priority_9,["jump_begin_water.ogg"]),
 ("jump_end_water", sf_vol_3|sf_priority_9,["jump_end_water.ogg"]),
 ("horse_jump_begin", sf_vol_6|sf_priority_9,["horse_jump_begin.ogg"]),
 ("horse_jump_end", sf_vol_7|sf_priority_9,["horse_jump_end.ogg"]),
 ("horse_jump_begin_water", sf_vol_6|sf_priority_9,["jump_begin_water.ogg"]),
 ("horse_jump_end_water", sf_vol_6|sf_priority_9,["jump_end_water.ogg"]),

 ("release_bow",sf_vol_4, ["bow_shoot_01.wav","bow_shoot_02.wav","bow_shoot_03.wav","bow_shoot_04.wav","bow_shoot_05.wav","bow_shoot_06.wav","bow_shoot_07.wav","bow_shoot_08.wav","bow_shoot_09.wav","bow_shoot_10.wav"]),
 ("release_crossbow",sf_vol_7, ["crossbow_shoot_01.wav","crossbow_shoot_02.wav","crossbow_shoot_03.wav","crossbow_shoot_04.wav","crossbow_shoot_05.wav","crossbow_shoot_06.wav",]),
 ("throw_javelin",sf_vol_5, ["throw_javelin_2.ogg"]),
 ("throw_axe",sf_vol_7, ["throw_axe_1.ogg"]),
 ("throw_knife",sf_vol_5, ["throw_knife_1.ogg"]),
 ("throw_stone",sf_vol_7, ["throw_stone_1.ogg"]),

 ("reload_crossbow",sf_vol_3, ["reload_crossbow_1.ogg"]),
 ("reload_crossbow_continue",sf_vol_6, ["put_back_dagger.ogg"]),
 ("pull_bow",sf_vol_5, ["pull_bow_1.ogg"]),
 ("pull_arrow",sf_vol_5, ["pull_arrow.ogg"]),

 ("arrow_pass_by",sf_priority_7, ["arrow_pass_01.wav","arrow_pass_02.wav","arrow_pass_03.wav","arrow_pass_04.wav","arrow_pass_05.wav","arrow_pass_06.wav","arrow_pass_07.wav","arrow_pass_08.wav","arrow_pass_09.wav","arrow_pass_10.wav"]),
 ("bolt_pass_by",sf_priority_7, ["bolt_pass_by_1.ogg"]),
 ("javelin_pass_by",sf_priority_7, ["javelin_pass_by_1.ogg","javelin_pass_by_2.ogg"]),
 ("stone_pass_by",sf_vol_9|sf_priority_7, ["stone_pass_by_1.ogg"]),
 ("axe_pass_by",sf_priority_7, ["axe_pass_by_1.ogg"]),
 ("knife_pass_by",sf_priority_7, ["knife_pass_by_1.ogg"]),
 ("bullet_pass_by",sf_priority_7, ["arrow_whoosh_1.ogg"]),
 
 ("incoming_arrow_hit_ground",sf_priority_7|sf_vol_7, ["arrow_hit_ground_2.ogg","arrow_hit_ground_3.ogg","incoming_bullet_hit_ground_1.ogg"]),
 ("incoming_bolt_hit_ground",sf_priority_7|sf_vol_7, ["arrow_hit_ground_2.ogg","arrow_hit_ground_3.ogg","incoming_bullet_hit_ground_1.ogg"]),
 ("incoming_javelin_hit_ground",sf_priority_7|sf_vol_7, ["incoming_javelin_hit_ground_1.ogg"]),
 ("incoming_stone_hit_ground",sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.ogg"]),
 ("incoming_axe_hit_ground",sf_priority_7|sf_vol_7, ["incoming_javelin_hit_ground_1.ogg"]),
 ("incoming_knife_hit_ground",sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.ogg"]),
 ("incoming_bullet_hit_ground",sf_priority_7|sf_vol_7, ["incoming_bullet_hit_ground_1.ogg"]),

 ("outgoing_arrow_hit_ground",sf_priority_7|sf_vol_7, ["outgoing_arrow_hit_ground.ogg"]),
 ("outgoing_bolt_hit_ground",sf_priority_7|sf_vol_7,  ["outgoing_arrow_hit_ground.ogg"]),
 ("outgoing_javelin_hit_ground",sf_priority_7|sf_vol_10, ["outgoing_arrow_hit_ground.ogg"]),
 ("outgoing_stone_hit_ground",sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.ogg"]),
 ("outgoing_axe_hit_ground",sf_priority_7|sf_vol_7, ["incoming_javelin_hit_ground_1.ogg"]),
 ("outgoing_knife_hit_ground",sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.ogg"]),
 ("outgoing_bullet_hit_ground",sf_priority_7|sf_vol_7, ["incoming_bullet_hit_ground_1.ogg"]),


 ("draw_sword",sf_priority_2|sf_vol_4, ["draw_sword.ogg"]),
 ("put_back_sword",sf_priority_1|sf_vol_4, ["put_back_sword.ogg"]),
 ("draw_greatsword",sf_priority_2|sf_vol_4, ["draw_greatsword.ogg"]),
 ("put_back_greatsword",sf_priority_1|sf_vol_4, ["put_back_sword.ogg"]),
 ("draw_axe",sf_priority_2|sf_vol_4, ["draw_mace.ogg"]),
 ("put_back_axe",sf_priority_1|sf_vol_4, ["put_back_to_holster.ogg"]),
 ("draw_greataxe",sf_priority_2|sf_vol_4, ["draw_greataxe.ogg"]),
 ("put_back_greataxe",sf_priority_1|sf_vol_4, ["put_back_to_leather.ogg"]),
 ("draw_spear",sf_priority_2|sf_vol_4, ["draw_spear.ogg"]),
 ("put_back_spear",sf_priority_1|sf_vol_4, ["put_back_to_leather.ogg"]),
 ("draw_crossbow",sf_priority_2|sf_vol_4, ["draw_crossbow.ogg"]),
 ("put_back_crossbow",sf_priority_1|sf_vol_4, ["put_back_to_leather.ogg"]),
 ("draw_revolver",sf_priority_2|sf_vol_4, ["draw_from_holster.ogg"]),
 ("put_back_revolver",sf_priority_1|sf_vol_4, ["put_back_to_holster.ogg"]),
 ("draw_dagger",sf_priority_2|sf_vol_4, ["draw_dagger.ogg"]),
 ("put_back_dagger",sf_priority_1|sf_vol_4, ["put_back_dagger.ogg"]),
 ("draw_bow",sf_priority_2|sf_vol_4, ["draw_bow.ogg"]),
 ("put_back_bow",sf_priority_1|sf_vol_4, ["put_back_to_holster.ogg"]),
 ("draw_shield",sf_priority_2|sf_vol_4, ["draw_shield.ogg"]),
 ("put_back_shield",sf_priority_1|sf_vol_4, ["put_back_shield.ogg"]),
 ("draw_other",sf_priority_2|sf_vol_4, ["draw_other.ogg"]),
 ("put_back_other",sf_priority_1|sf_vol_4, ["draw_other2.ogg"]),

 ("body_fall_small",sf_priority_5|sf_vol_9, ["body_fall_small_01.wav","body_fall_small_02.wav","body_fall_small_03.wav","body_fall_small_04.wav","body_fall_small_05.wav","body_fall_small_06.wav","body_fall_small_07.wav","body_fall_small_08.wav"]),
 ("body_fall_big",sf_priority_6|sf_vol_8, ["body_fall_large_01.wav","body_fall_large_02.wav","body_fall_large_03.wav","body_fall_large_04.wav","body_fall_large_05.wav","body_fall_large_06.wav","body_fall_large_07.wav","body_fall_large_08.wav"]),
# ("body_fall_very_big",sf_priority_9|sf_vol_10, ["body_fall_very_big_1.ogg"]),
 ("horse_body_fall_begin",sf_priority_6|sf_vol_10, ["horse_body_fall_begin_1.ogg"]),
 ("horse_body_fall_end",sf_priority_6|sf_vol_10, ["horse_body_fall_end_1.ogg","body_fall_2.ogg","body_fall_very_big_1.ogg"]),
 
## ("clang_metal",sf_priority_9, ["clang_metal_1.ogg","clang_metal_2.ogg","s_swordClash1.wav","s_swordClash2.wav","s_swordClash3.wav"]),
 ("hit_wood_wood",sf_priority_7|sf_vol_12, ["hit_wood_wood_1.ogg","hit_wood_wood_2.ogg","hit_wood_wood_3.ogg","hit_wood_wood_4.ogg","hit_wood_metal_4.ogg","hit_wood_metal_5.ogg","hit_wood_metal_6.ogg"]),#dummy
 ("hit_metal_metal",sf_priority_7|sf_vol_10, ["hit_metal_metal_3.ogg","hit_metal_metal_4.ogg",
                                              "hit_metal_metal_5.ogg","hit_metal_metal_6.ogg","hit_metal_metal_7.ogg","hit_metal_metal_8.ogg",
                                              "hit_metal_metal_9.ogg","hit_metal_metal_10.ogg",
                                              "clang_metal_1.ogg","clang_metal_2.ogg"]),
 ("hit_wood_metal",sf_priority_7|sf_vol_10, ["hit_metal_metal_1.ogg","hit_metal_metal_2.ogg","hit_wood_metal_7.ogg"]),
# ("clang_metal", sf_priority_9,["sword_clank_metal_09.ogg","sword_clank_metal_10.ogg","sword_clank_metal_12.ogg","sword_clank_metal_13.ogg"]),
## ("shield_hit_cut",sf_priority_5, ["shield_hit_cut_3.ogg","shield_hit_cut_4.ogg","shield_hit_cut_5.ogg"]),
 ("shield_hit_wood_wood",sf_priority_7|sf_vol_9, ["shield_hit_wood_wood_1.ogg","shield_hit_wood_wood_2.ogg","shield_hit_wood_wood_3.ogg"]),
 ("shield_hit_metal_metal",sf_priority_7|sf_vol_10, ["shield_hit_metal_metal_1.ogg","shield_hit_metal_metal_2.ogg","shield_hit_metal_metal_3.ogg","shield_hit_metal_metal_4.ogg"]),
 ("shield_hit_wood_metal",sf_priority_7|sf_vol_10, ["shield_hit_cut_3.ogg","shield_hit_cut_4.ogg","shield_hit_cut_5.ogg","shield_hit_cut_10.ogg"]), #(shield is wood)
 ("shield_hit_metal_wood",sf_priority_7|sf_vol_10, ["shield_hit_metal_wood_1.ogg","shield_hit_metal_wood_2.ogg","shield_hit_metal_wood_3.ogg"]),#(shield is metal)
 ("shield_broken",sf_priority_9, ["shield_break_01.wav","shield_break_02.wav"]),
 ("man_hit",sf_priority_7|sf_vol_7, ["man_hit_5.ogg","man_hit_6.ogg","man_hit_7.ogg","man_hit_8.ogg","man_hit_9.ogg","man_hit_10.ogg","man_hit_11.ogg","man_hit_12.ogg","man_hit_13.ogg","man_hit_14.ogg","man_hit_15.ogg",
                                      "man_hit_17.ogg","man_hit_18.ogg","man_hit_19.ogg","man_hit_22.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg","man_hit_59.ogg"]),
 ("man_die",sf_priority_10|sf_vol_8,  ["man_die_01.mp3","man_die_02.mp3","man_die_03.mp3","man_die_04.mp3","man_die_05.mp3","man_die_06.wav","man_die_07.wav","man_die_08.wav","man_die_09.wav","man_die_10.wav","man_die_11.wav","man_die_12.wav","man_die_13.wav","man_die_14.wav","man_die_15.wav","man_die_16.wav","man_die_17.wav","man_die_18.wav","man_die_19.wav","man_die_20.wav","man_die_21.wav","man_die_22.wav","man_die_23.wav","man_die_24.wav","man_die_25.wav","man_die_26.wav","man_die_27.wav","man_die_28.wav","man_die_29.wav","man_die_31.wav","man_die_32.wav"]),
 ("woman_hit",sf_priority_7, ["woman_hit_2.ogg","woman_hit_3.ogg",
                              "woman_hit_b_2.ogg","woman_hit_b_4.ogg","woman_hit_b_6.ogg","woman_hit_b_7.ogg","woman_hit_b_8.ogg",
                              "woman_hit_b_11.ogg","woman_hit_b_14.ogg","woman_hit_b_16.ogg"]),
 ("woman_die",sf_priority_10|sf_vol_9, ["woman_fall_1.ogg","woman_hit_b_5.ogg"]),
 ("woman_yell",sf_priority_8|sf_vol_9, ["woman_yell_1.ogg","woman_yell_2.ogg"]),
 ("hide",0, ["s_hide.wav"]),
 ("unhide",0, ["s_unhide.wav"]),
 ("neigh",0, ["horse_exterior_whinny_01.ogg","horse_exterior_whinny_02.ogg","horse_exterior_whinny_03.ogg","horse_exterior_whinny_04.ogg","horse_exterior_whinny_05.ogg","horse_whinny.ogg"]),
 ("gallop",sf_vol_4, ["horse_gallop_3.ogg","horse_gallop_4.ogg","horse_gallop_5.ogg"]),
 ("battle",sf_vol_4, ["battle.wav"]),
# ("bow_shoot_player",sf_priority_10|sf_vol_10, ["bow_shoot_4.ogg"]),
# ("bow_shoot",sf_priority_4, ["bow_shoot_4.ogg"]),
# ("crossbow_shoot",sf_priority_4, ["bow_shoot_2.ogg"]),
 ("arrow_hit_body",sf_priority_4, ["arrow_hit_body_1.ogg","arrow_hit_body_2.ogg","arrow_hit_body_3.ogg"]),
 ("metal_hit_low_armor_low_damage",sf_priority_5|sf_vol_9, ["metal_low_low_01.wav","metal_low_low_02.wav","metal_low_low_03.wav","metal_low_low_04.wav","metal_low_low_05.wav","metal_low_low_06.wav","metal_low_low_08.wav"]),
 ("metal_hit_low_armor_high_damage",sf_priority_5|sf_vol_9, ["metal_low_high_01.wav","metal_low_high_02.wav","metal_low_high_03.wav","metal_low_high_04.wav","metal_low_high_05.wav","metal_low_high_06.wav","metal_low_high_08.wav","metal_low_high_09.wav"]),
 ("metal_hit_high_armor_low_damage",sf_priority_5|sf_vol_9, ["metal_high_low_01.wav","metal_high_low_02.wav","metal_high_low_03.wav","metal_high_low_04.wav","metal_high_low_05.wav","metal_high_low_06.wav","metal_high_low_07.wav","metal_high_low_08.wav","metal_high_low_09.wav","metal_high_low_10.wav","metal_high_low_11.wav","metal_high_low_12.wav","metal_high_low_13.wav","metal_high_low_14.wav","metal_high_low_15.wav","metal_high_low_16.wav","metal_high_low_17.wav","metal_high_low_18.wav","metal_high_low_19.wav","metal_high_low_20.wav","metal_high_low_21.wav","metal_high_low_22.wav","metal_high_low_23.wav","metal_high_low_24.wav","metal_high_low_25.wav"]),
 ("metal_hit_high_armor_high_damage",sf_priority_5|sf_vol_9, ["metal_high_high_01.wav","metal_high_high_02.wav","metal_high_high_03.wav","metal_high_high_04.wav","metal_high_high_05.wav","metal_high_high_06.wav","metal_high_high_07.wav","metal_high_high_08.wav","metal_high_high_09.wav","metal_high_high_10.wav","metal_high_high_11.wav","metal_high_high_12.wav","metal_high_high_13.wav","metal_high_high_14.wav","metal_high_high_15.wav","metal_high_high_16.wav","metal_high_high_17.wav","metal_high_high_18.wav","metal_high_high_19.wav","metal_high_high_20.wav","metal_high_high_21.wav","metal_high_high_22.wav","metal_high_high_23.wav","metal_high_high_24.wav","metal_high_high_25.wav","metal_high_high_26.wav","metal_high_high_27.wav","metal_high_high_28.wav","metal_high_high_29.wav","metal_high_high_30.wav","metal_high_high_31.wav","metal_high_high_32.wav"]),
 ("wooden_hit_low_armor_low_damage",sf_priority_5|sf_vol_9, ["blunt_hit_low_1.ogg","blunt_hit_low_2.ogg","blunt_hit_low_3.ogg"]),
 ("wooden_hit_low_armor_high_damage",sf_priority_5|sf_vol_9, ["blunt_hit_high_1.ogg","blunt_hit_high_2.ogg","blunt_hit_high_3.ogg"]),
 ("wooden_hit_high_armor_low_damage",sf_priority_5|sf_vol_9, ["wooden_hit_high_armor_low_damage.ogg","wooden_hit_high_armor_low_damage_2.ogg"]),
 ("wooden_hit_high_armor_high_damage",sf_priority_5|sf_vol_9, ["blunt_hit_high_1.ogg","blunt_hit_high_2.ogg","blunt_hit_high_3.ogg"]),
 ("mp_arrow_hit_target",sf_2d|sf_priority_15|sf_vol_9, ["mp_arrow_hit_target.ogg"]),
 ("blunt_hit",sf_priority_5|sf_vol_9, ["punch_1.ogg","punch_4.ogg","punch_4.ogg","punch_5.ogg"]),
 ("player_hit_by_arrow",sf_priority_10|sf_vol_10, ["player_hit_by_arrow.ogg"]),
 ("pistol_shot",sf_priority_10|sf_vol_10, ["fl_pistol.wav"]),
 ("man_grunt",sf_priority_6|sf_vol_4, ["man_excercise_1.ogg","man_excercise_2.ogg","man_excercise_4.ogg"]),
 ("man_breath_hard",sf_priority_3|sf_vol_8, ["man_ugh_1.ogg","man_ugh_2.ogg","man_ugh_4.ogg","man_ugh_7.ogg","man_ugh_12.ogg","man_ugh_13.ogg","man_ugh_17.ogg"]),
 ("man_stun",sf_priority_3|sf_vol_8, ["man_stun_1.ogg"]),
 ("man_grunt_long",sf_priority_6|sf_vol_7, ["man_grunt_1.ogg","man_grunt_2.ogg","man_grunt_3.ogg","man_grunt_5.ogg","man_grunt_13.ogg","man_grunt_14.ogg"]),
 ("man_yell",sf_priority_5|sf_vol_8, ["man_yell_4.ogg","man_yell_4_2.ogg","man_yell_7.ogg","man_yell_9.ogg","man_yell_11.ogg","man_yell_13.ogg","man_yell_15.ogg","man_yell_16.ogg","man_yell_17.ogg","man_yell_20.ogg","man_shortyell_4.ogg","man_shortyell_5.ogg","man_shortyell_6.ogg","man_shortyell_9.ogg","man_shortyell_11.ogg","man_shortyell_11b.ogg",
                        "man_yell_b_18.ogg","man_yell_22.ogg", "man_yell_c_20.ogg"]),
## not adequate, removed: "man_yell_b_21.ogg","man_yell_b_22.ogg","man_yell_b_23.ogg"]),
#TODONOW:
 ("man_warcry",sf_priority_5, ["man_insult_2.ogg","man_insult_3.ogg","man_insult_7.ogg","man_insult_9.ogg","man_insult_13.ogg","man_insult_15.ogg","man_insult_16.ogg"]),

 ("encounter_looters",sf_2d|sf_vol_8, ["encounter_river_pirates_5.ogg","encounter_river_pirates_6.ogg","encounter_river_pirates_9.ogg","encounter_river_pirates_10.ogg","encounter_river_pirates_4.ogg"]),

 ("encounter_bandits",sf_2d|sf_vol_8, ["encounter_bandit_2.ogg","encounter_bandit_9.ogg","encounter_bandit_12.ogg","encounter_bandit_13.ogg","encounter_bandit_15.ogg","encounter_bandit_16.ogg","encounter_bandit_10.ogg",]),
 ("encounter_farmers",sf_2d|sf_vol_8, ["encounter_farmer_2.ogg","encounter_farmer_5.ogg","encounter_farmer_7.ogg","encounter_farmer_9.ogg"]),
 ("encounter_sea_raiders",sf_2d|sf_vol_8, ["encounter_sea_raider_5.ogg","encounter_sea_raider_9.ogg","encounter_sea_raider_9b.ogg","encounter_sea_raider_10.ogg"]),
 ("encounter_steppe_bandits",sf_2d|sf_vol_8, ["encounter_steppe_bandit_3.ogg","encounter_steppe_bandit_3b.ogg","encounter_steppe_bandit_8.ogg","encounter_steppe_bandit_10.ogg","encounter_steppe_bandit_12.ogg"]),
 ("encounter_nobleman",sf_2d|sf_vol_8, ["encounter_nobleman_1.ogg"]),
 ("encounter_vaegirs_ally",sf_2d|sf_vol_8, ["encounter_vaegirs_ally.ogg","encounter_vaegirs_ally_2.ogg"]),
 ("encounter_vaegirs_neutral",sf_2d|sf_vol_8, ["encounter_vaegirs_neutral.ogg","encounter_vaegirs_neutral_2.ogg","encounter_vaegirs_neutral_3.ogg","encounter_vaegirs_neutral_4.ogg"]),
 ("encounter_vaegirs_enemy",sf_2d|sf_vol_8, ["encounter_vaegirs_neutral.ogg","encounter_vaegirs_neutral_2.ogg","encounter_vaegirs_neutral_3.ogg","encounter_vaegirs_neutral_4.ogg"]),
 ("sneak_town_halt",sf_2d, ["sneak_halt_1.ogg","sneak_halt_2.ogg"]),
 ("horse_walk",sf_priority_3|sf_vol_5, ["horse_walk_1.ogg","horse_walk_2.ogg","horse_walk_3.ogg","horse_walk_4.ogg"]),
 ("horse_trot",sf_priority_4|sf_vol_6, ["horse_trot_1.ogg","horse_trot_2.ogg","horse_trot_3.ogg","horse_trot_4.ogg"]),
 ("horse_canter",sf_priority_4|sf_vol_7, ["horse_canter_1.ogg","horse_canter_2.ogg","horse_canter_3.ogg","horse_canter_4.ogg"]),
 ("horse_gallop",sf_priority_5|sf_vol_8, ["horse_gallop_06.wav","horse_gallop_07.wav","horse_gallop_08.wav","horse_gallop_09.wav"]),
 ("horse_breath",sf_priority_1|sf_vol_4, ["horse_breath_4.ogg","horse_breath_5.ogg","horse_breath_6.ogg","horse_breath_7.ogg"]),
 ("horse_snort",sf_priority_1|sf_vol_2, ["horse_snort_1.ogg","horse_snort_2.ogg","horse_snort_3.ogg","horse_snort_4.ogg","horse_snort_5.ogg"]),
 ("horse_low_whinny",sf_vol_12, ["horse_whinny-1.ogg","horse_whinny-2.ogg"]),
 ("block_fist",0, ["block_fist_3.ogg","block_fist_4.ogg"]),
 ("man_hit_blunt_weak",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_hit_blunt_strong",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_hit_pierce_weak",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_hit_pierce_strong",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_hit_cut_weak",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_hit_cut_strong",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_victory",sf_priority_5|sf_vol_10, ["man_victory_3.ogg","man_victory_4.ogg","man_victory_5.ogg","man_victory_8.ogg","man_victory_15.ogg","man_victory_49.ogg","man_victory_52.ogg","man_victory_54.ogg","man_victory_57.ogg","man_victory_71.ogg","man_victory_1.mp3","man_victory_2.mp3","man_victory_3.mp3","man_victory_4.mp3","man_victory_5.mp3"]),
 ("fire_loop",sf_priority_9|sf_vol_4|sf_looping|sf_start_at_random_pos, ["Fire_Torch_Loop3.wav","Fire_Torch_Loop2.wav"]),
 ("torch_loop",sf_priority_9|sf_vol_4|sf_looping|sf_start_at_random_pos, ["Fire_Torch_Loop3.ogg","Fire_Torch_Loop2.wav"]),
 ("dummy_hit",sf_priority_9, ["shield_hit_cut_3.ogg","shield_hit_cut_5.ogg"]),
 ("dummy_destroyed",sf_priority_9, ["shield_broken.ogg"]),
 ("gourd_destroyed",sf_priority_9, ["shield_broken.ogg"]),#TODO
 ("cow_moo", sf_2d|sf_priority_9|sf_vol_8, ["cow_moo_1.ogg"]),
 ("cow_slaughter", sf_2d|sf_priority_9|sf_vol_8, ["cow_slaughter.ogg"]),
 ("distant_dog_bark", sf_2d|sf_priority_3|sf_vol_8, ["d_dog1.ogg","d_dog2.ogg","d_dog3.ogg","d_dog7.ogg"]),
 ("distant_owl", sf_2d|sf_priority_3|sf_vol_9, ["d_owl2.wav","d_owl3.wav","d_owl4.wav"]),
 ("distant_chicken", sf_2d|sf_priority_3|sf_vol_8, ["d_chicken1.ogg","d_chicken2.ogg"]),
 ("distant_carpenter", sf_2d|sf_priority_3|sf_vol_3, ["d_carpenter1.wav","d_saw_short3.wav"]),
 ("distant_blacksmith", sf_2d|sf_priority_3|sf_vol_4, ["d_blacksmith2.wav"]),
 ("arena_ambiance", sf_2d|sf_priority_8|sf_vol_3|sf_looping, ["arena_loop11.ogg"]),
 ("town_ambiance", sf_2d|sf_priority_8|sf_vol_3|sf_looping, ["town_loop_3.wav"]),
 ("tutorial_fail", sf_2d|sf_vol_7,["cue_failure.ogg"]),
 ("your_flag_taken", sf_2d|sf_priority_10|sf_vol_10, ["your_flag_taken.ogg"]),
 ("enemy_flag_taken", sf_2d|sf_priority_10|sf_vol_10, ["enemy_flag_taken.ogg"]),
 ("flag_returned", sf_2d|sf_priority_10|sf_vol_10, ["your_flag_returned.ogg"]),
 ("team_scored_a_point", sf_2d|sf_priority_10|sf_vol_10, ["you_scored_a_point.ogg"]),
 ("enemy_scored_a_point", sf_2d|sf_priority_10|sf_vol_10, ["enemy_scored_a_point.ogg"]),
 ("dedal_tavern_lute",	sf_priority_6|sf_vol_5|sf_looping, ["dedal_tavern_lute_1.ogg","dedal_tavern_lute_2.ogg","dedal_tavern_lute_3.ogg"]),
 ("dedal_tavern_lyre",	sf_priority_6|sf_vol_6|sf_looping, ["dedal_tavern_lyre_1.ogg","dedal_tavern_lyre_2.ogg","dedal_tavern_lyre_3.ogg"]),
]
