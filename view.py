from tkinter import LabelFrame, Label, LEFT

from utils import give_me_a_random_phrase

# Design colours
background_colour = "#001336"
dark_text_colour = "#1e1e21"
bright_text_colour = "#f2ece6"
user_input_colour = "#c77f14"
window_background = "#000000"


# Design text settings
title_font_size = 35
default_text_size = 13
default_font_family = "Arial Rounded MT Bold"


def print_random_phrase(output_frame, current_stage_score: int, current_level_score: int, game_is_running) -> None:
    current_random_phrase = give_me_a_random_phrase(15 + current_stage_score*10, current_level_score)
    add_to_output(output_frame, current_random_phrase, False, True, game_is_running)
    print(current_random_phrase)


def add_to_output(output_frame: LabelFrame, str_to_print, is_user_input, user_input_after, game_is_running: bool):
    if output_frame.children.__len__() > 12:
        count = 0
        for child in output_frame.winfo_children():
            if count < output_frame.children.__len__() - 3:
                child.destroy()

    # Displays message if the user tries to enter something while the game is not yet running
    if not game_is_running and is_user_input:
        text_to_add_label = Label(output_frame, text="The game hasn't started yet. Click \"Start Game\" to start the game", bg=background_colour, fg=bright_text_colour)
        text_to_add_label.config(font=(default_font_family, default_text_size))
        text_to_add_label.pack(padx=10, anchor="w")
        return

    # Changes the last child in the LabelFrame according to the users input if the game is running
    if game_is_running and is_user_input and user_input_after:
        output_frame.winfo_children()[output_frame.winfo_children().__len__() - 1].config(text="> " + str_to_print)
        new_line_label = Label(output_frame, text="> ", bg=background_colour, fg=user_input_colour,
                               wraplength=output_frame.winfo_width()-20, justify=LEFT)
        new_line_label.config(font=(default_font_family, default_text_size))
        new_line_label.pack(padx=10, anchor="w")
        return

    if game_is_running and is_user_input and not user_input_after:
        output_frame.winfo_children()[output_frame.winfo_children().__len__() - 1].config(text="> " + str_to_print)
        return

    if not is_user_input and not user_input_after:
        text_to_add_label = Label(output_frame, text=str_to_print, bg=background_colour, fg=bright_text_colour,
                                  wraplength=output_frame.winfo_width() - 20, justify=LEFT)
        text_to_add_label.config(font=(default_font_family, default_text_size))
        text_to_add_label.pack(padx=10, anchor="w")

    if not is_user_input and user_input_after:
        text_to_add_label = Label(output_frame, text=str_to_print, bg=background_colour, fg=bright_text_colour,
                                  wraplength=output_frame.winfo_width()-20, justify=LEFT)
        text_to_add_label.config(font=(default_font_family, default_text_size))
        text_to_add_label.pack(padx=10, anchor="w")

        new_line_label = Label(output_frame, text="> ", bg=background_colour, fg=user_input_colour,
                               wraplength=output_frame.winfo_width()-20, justify=LEFT)
        new_line_label.config(font=(default_font_family, default_text_size))
        new_line_label.pack(padx=10, anchor="w")