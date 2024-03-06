# count_messages

This small project counts the amount of matches of a given string (by default, the poo emoji) per person in a month from a WhatsApp chat log export.

It takes in a text file containing the chat logs from WhatsApp, which has a default format of

```py
[{DAY}/{MONTH}/{YEAR} {HOURS}:{MINUTES}:{SECONDS}] {USERNAME}: {MESSAGE}
```

Then parses the lines from the file to count the matches and saves them in a defaultdict to increment the count, arranged per month, per person.

It outputs the sorted result of counts per month, in order from greatest to lowest.

## Usage

To clone and run this project, you'll need `git` and `python` installed on your computer.
You'll also need a chat log from WhatsApp (which you can export from your phone, on the chat details screen). Inside the .zip file from the export you'll find a `_chat.txt` file, which contains the chat logs.

From which, just do the following steps:

```sh
# Clone this repository
$ git clone https://github.com/scramblerdoodle/count_messages.git

# Go into the repository
$ cd count_messages
```

Then, preferably move the `_chat.txt` file into the same folder as the project, and finally:

```sh
# Run the project
$ python count_messages.py
```

It also takes in two optional command line arguments, as follows:

```sh
python count_messages.py [string_to_match] [file_path]
```

If no argument is provided, the default values are used (`string_to_match` as the poo emoji, `file_path` as the `_chat.txt` file in the same folder).

If one argument is provided, it replaces `string_to_match` with the provided string.

If two arguments are provided, they replace `string_to_match` and `file_path`.

Should one want to seek a space-separated string, you'll need to encapsulate them with quotation marks, for example:

```sh
python count_messages.py "good morning"
```
Which will read the `_chat.txt` file and return the count of occurrences of "good morning" per person.
