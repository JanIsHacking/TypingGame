from tkinter import *
from view import add_to_output, print_random_phrase, background_colour, window_background, default_text_size, default_font_family, bright_text_colour, dark_text_colour, title_font_size


starting_lives = 3

# Setting up level, stage and remaining level scores
current_level_score = 1
current_stage_score = 1
remaining_lives_score = starting_lives
start_game_button_state = NORMAL
game_is_running = False
current_random_phrase = ""


def start_game():
    global start_game_button_state
    global game_is_running
    global current_random_phrase
    global current_level_score
    global current_stage_score
    global remaining_lives_score

    current_level_score = 1
    current_stage_score = 1
    remaining_lives_score = starting_lives

    update_score_labels()

    if not game_is_running:
        game_is_running = True
        add_to_output(output_frame, "Welcome to the typing game! Have fun!", False, False, game_is_running)
        add_to_output(output_frame, "Type this string into the input prompt and hit Enter:", False, False, game_is_running)

        print_random_phrase(output_frame, current_stage_score, current_level_score, game_is_running)

        start_game_button.config(state=DISABLED)


# Initializing the window and making basic settings
root = Tk()
root.title("Typing Game")
root.geometry("1200x675")
root.configure(background=window_background)

# Creating all the labels and buttons
main_frame = Frame(root, bg=background_colour, highlightbackground=bright_text_colour, highlightthickness=1)
main_frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

header_label = Label(main_frame, text="Typing Game", bg=background_colour, fg=bright_text_colour)
header_label.config(font=(default_font_family, title_font_size, "bold"))

input_label = Label(main_frame, text="Input prompt: ", anchor="w", bg=background_colour, fg=bright_text_colour)
input_label.config(font=(default_font_family, default_text_size))

user_entry = Entry(main_frame)

start_game_button = Button(main_frame,command=start_game, text="Start Game", bg=dark_text_colour, fg=bright_text_colour,
                           highlightbackground=bright_text_colour, highlightthickness=1, state=start_game_button_state)

# Level label and stuff
current_level_label = Label(main_frame, text="Current Level: ", bg=background_colour, fg=bright_text_colour)
current_level_label.config(font=(default_font_family, default_text_size))
current_level_score_label = Label(main_frame, text=current_level_score, bg=background_colour, fg=bright_text_colour)
current_level_score_label.config(font=(default_font_family, default_text_size))

# Stage label and stuff
current_stage_label = Label(main_frame, text="Current Stage: ", bg=background_colour, fg=bright_text_colour)
current_stage_label.config(font=(default_font_family, default_text_size))
current_stage_score_label = Label(main_frame, text=current_stage_score, bg=background_colour, fg=bright_text_colour)
current_stage_score_label.config(font=(default_font_family, default_text_size))

# Lives remaining label and stuff
remaining_lives_label = Label(main_frame, text="Lives remaining: ", bg=background_colour, fg=bright_text_colour)
remaining_lives_label.config(font=(default_font_family, default_text_size))
remaining_lives_score_label = Label(main_frame, text=remaining_lives_score, bg=background_colour, fg=bright_text_colour)
remaining_lives_score_label.config(font=(default_font_family, default_text_size))

output_frame = LabelFrame(main_frame, text=" Output: ", bg=background_colour, fg=bright_text_colour)
output_frame.config(font=(default_font_family, default_text_size))

# Putting all the labels and buttons on the screen
header_label.place(relwidth=0.6, relheight=0.2, relx=0.2, rely=0)
input_label.place(relwidth=0.31, relheight=0.05, relx=0.01, rely=0.23)
user_entry.place(relwidth=0.31, relheight=0.05, relx=0.01, rely=0.3)
start_game_button.place(relwidth=0.1, relheight=0.05, relx=0.02, rely=0.75)
current_level_label.place(relwidth=0.33, relheight=0.1, relx=0, rely=0.9)
current_level_score_label.place(relwidth=0.01, relheight=0.1, relx=0.25, rely=0.9)
current_stage_label.place(relwidth=0.33, relheight=0.1, relx=0.33, rely=0.9)
current_stage_score_label.place(relwidth=0.01, relheight=0.1, relx=0.58, rely=0.9)
remaining_lives_label.place(relwidth=0.34, relheight=0.1, relx=0.66, rely=0.9)
remaining_lives_score_label.place(relwidth=0.01, relheight=0.1, relx=0.92, rely=0.9)
output_frame.place(relwidth=0.64, relheight=0.7, relx=0.34, rely=0.2)


def compare_strings_and_take_action(users_string):
    global game_is_running
    global current_level_score
    global current_stage_score
    global remaining_lives_score

    if not game_is_running:
        return

    if users_string == current_random_phrase:
        if current_stage_score == 3:
            if current_level_score == 4:
                add_to_output(output_frame, "You won the game! You really are a pro at typing!", False, False, game_is_running)
                add_to_output(output_frame, "Press \"Start Game\" to play again", False, False, game_is_running)
                game_is_running = False
                start_game_button.config(state=NORMAL)
                return
            current_level_score += 1
            current_stage_score = 1
            add_to_output(output_frame, "Nice, you made this level. Good luck with the next one!", False, False, game_is_running)
            print_random_phrase(output_frame, current_stage_score, current_level_score, game_is_running)
            update_score_labels()
            return
        current_stage_score += 1
        add_to_output(output_frame, "Not bad, try the next stage.", False, False, game_is_running)
        print_random_phrase(output_frame, current_stage_score, current_level_score, game_is_running)
        update_score_labels()
        return

    remaining_lives_score -= 1
    if remaining_lives_score == 2:
        add_to_output(output_frame, "You got 2 lives left. Better don't fail again!", False, False, game_is_running)
        update_score_labels()
    elif remaining_lives_score == 1:
        add_to_output(output_frame, "1 life to go ...", False, False, game_is_running)
        update_score_labels()
    elif remaining_lives_score == 0:
        add_to_output(output_frame, "You lost. Keep it up!", False, False, game_is_running)
        game_is_running = False
        update_score_labels()
        start_game_button.config(state=NORMAL)
        return

    print_random_phrase(output_frame, current_stage_score, current_level_score, game_is_running)


def update_score_labels():
    current_level_score_label.config(text=current_level_score)
    current_stage_score_label.config(text=current_stage_score)
    remaining_lives_score_label.config(text=remaining_lives_score)


def user_hit_return(event):
    if user_entry.focus_get():
        add_to_output(output_frame, user_entry.get(), True, False, game_is_running)
    compare_strings_and_take_action(user_entry.get())
    user_entry.delete(0, "end")


def main():
    root.bind("<Return>", user_hit_return)

    # Starting the program
    root.mainloop()


if __name__ == '__main__':
    main()
