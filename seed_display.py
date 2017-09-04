""" seed_display.py displays details about the SEED data """

import json
import random

import seed
import seed_lookup
import seed_process

MARKDOWN_HEADER_MARKER = "---"
MARKDOWN_PERSON_NAME = "person_name"
MARKDOWN_QUOTE = "\""
MARKDOWN_SECTION_MARKER = "#"

MARKDOWN_LAYOUT = "layout: blog_n"
MARKDOWN_TITLE = "title: SEED Interview with"
MARKDOWN_CATEGORIES = "categories: [seed, interview, software]"
MARKDOWN_PAGE_TITLE = "{{page.title}}"

QUESTION_FACT_FULL = "What is one fun fact that you can share about your company or a current project?"
QUESTION_CHALLENGE_FULL = "What is the greatest challenge that you face when working in your field?"
QUESTION_ADVICE_FULL = "What is one point of advice that you can give to people who plan to enter your field?"

TWO_SPACE_ENDING = ".  "
ONE_SPACE_ENDING = ". "


def seed_display_respondents(seed_dictionary_list):
    """ Displays all of the people who responded """
    sorted_seed_dictionary_list = seed_process.seed_process_sort_dictionary_list(
        seed_dictionary_list, seed_lookup.PERSON_NAME)
    print("Displaying the", len(sorted_seed_dictionary_list), "respondents")
    print()
    for current_seed_dictionary in sorted_seed_dictionary_list:
        current_name = current_seed_dictionary[seed_lookup.PERSON_NAME]
        current_company = current_seed_dictionary[seed_lookup.COMPANY_NAME]
        current_title = current_seed_dictionary[seed_lookup.TITLE_NAME]
        print(seed.INDENT,
              current_name.strip(), "is a",
              current_title.strip(), "at", current_company.strip())


def seed_display_respondent_markdown(seed_dictionary):
    """ Displays the details about a respondent """

    print(MARKDOWN_HEADER_MARKER)
    print(MARKDOWN_LAYOUT)
    print(MARKDOWN_CATEGORIES)
    seed_display_markdown_header_entry(seed_lookup.PERSON_NAME,
                                       seed_dictionary)
    seed_display_markdown_header_entry(seed_lookup.COMPANY_NAME,
                                       seed_dictionary)
    seed_display_markdown_header_entry(seed_lookup.TITLE_NAME, seed_dictionary)
    seed_display_markdown_header_entry(seed_lookup.WEB_SITE, seed_dictionary)
    print(MARKDOWN_HEADER_MARKER)
    print()
    print(MARKDOWN_SECTION_MARKER, MARKDOWN_PAGE_TITLE)
    print()
    print(MARKDOWN_SECTION_MARKER + MARKDOWN_SECTION_MARKER,
          QUESTION_FACT_FULL)
    print()
    print(seed_dictionary[seed_lookup.QUESITON_FACT].replace(
        TWO_SPACE_ENDING, ONE_SPACE_ENDING))
    print()
    print(MARKDOWN_SECTION_MARKER + MARKDOWN_SECTION_MARKER,
          QUESTION_CHALLENGE_FULL)
    print()
    print(seed_dictionary[seed_lookup.QUESTION_CHALLENGE])
    print()
    print(MARKDOWN_SECTION_MARKER + MARKDOWN_SECTION_MARKER,
          QUESTION_ADVICE_FULL)
    print()
    print(seed_dictionary[seed_lookup.QUESTION_ADVICE])
    print()


def seed_display_markdown_header_entry(seed_entry, seed_dictionary):
    """ Display a specific header entry """
    if seed_entry is not seed_lookup.PERSON_NAME:
        print(
            seed_entry,
            ": ",
            MARKDOWN_QUOTE,
            seed_dictionary[seed_entry].strip(),
            MARKDOWN_QUOTE,
            sep='')
    else:
        print(MARKDOWN_TITLE, " ", seed_dictionary[seed_entry].strip(), sep='')


def seed_display_sample(seed_dictionary_list):
    """ Displays all of the topics in a textual format """
    first_entry_index = 0
    last_entry_index = len(seed_dictionary_list)
    randomly_chosen_index = random.randint(first_entry_index, last_entry_index)
    first_seed_dictionary = seed_dictionary_list[randomly_chosen_index]
    print(json.dumps(first_seed_dictionary, indent=3))
