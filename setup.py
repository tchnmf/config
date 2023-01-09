#!/usr/bin/env python


# TODO:
# * Check if program the executable exists before attemptig to configure, ie which fish, which tmux

import os
import requests

home      = os.environ['HOME']+'/'

# def usage():
#     print()

def url_to_file(source_url,destination_file ):
    response=requests.get(source_url)
    with open(destination_file, 'w') as file:
        file.write(response.text)
        file.close()

def setup_fish():
    print('Configuring fish...')
    fish_variables_path = home+'/.config/fish/fish_variables-v2'
    fish_functions_path = home+'/.config/fish/functions/'
    fish_variables_url = 'https://raw.githubusercontent.com/tchnmf/config/master/fish/fish_variables'
    fish_functions_url = 'https://raw.githubusercontent.com/tchnmf/config/master/fish/functions/'
    fish_functions_list = [
        'fish_prompt.fish',
    ]
    # randomize color if fish prompt ?

    url_to_file(fish_variables_url, fish_variables_path)

    for fish_function in fish_functions_list:
        function_url = fish_functions_url + fish_function
        function_name = fish_function+'v2'
        function_path = fish_functions_path + function_name
        # print(function_path, function_url)
        url_to_file(function_url, function_path)
    print('Done.')

def setup_tmux():
    print('Configuring tmux...')
    conf_file_url = 'https://raw.githubusercontent.com/tchnmf/config/master/tmux/tmux.conf'
    conf_file_path = home+'/.tmux.conf'
    url_to_file(conf_file_url, conf_file_path)
    print('Done.')

def setup_vim():
    print('Configuring vim...')
    vimrc_url = 'https://raw.githubusercontent.com/tchnmf/config/master/vim/vimrc'
    vimrc_path = home+'/.vimrc'
    url_to_file(vimrc_url, vimrc_path)
    print('Done.')

def setup_ranger():
    print('Configuring ranger...')
    rc_url = 'https://raw.githubusercontent.com/tchnmf/config/master/ranger/rc.conf'
    rc_path = home+'/.config/ranger/rc.conf'
    url_to_file(rc_url, rc_path)
    print('Done.')


def main():
    setup_fish()
    setup_tmux()
    setup_vim()
    setup_ranger()


if __name__ == "__main__":
    main()


