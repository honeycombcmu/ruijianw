import json
INPUT_FILE = "test_set.txt"
OUTPUT_FILE = "test_set.json"
def raw2json(input=INPUT_FILE, output=OUTPUT_FILE, separator = "||"):
    """
    Transform the raw data into json type, which can be used for the
    Python wrapper of the Natural Language Classifier.
    Format: sentence||label   or    sentence(self-defined separator)label
    :param input: the path of input file
    :param output: the path of output file
    :param separator: the way you choose to use to separate the sentence and label
    :return: just generate the output file into output path
    """
    with open(INPUT_FILE, 'r') as input_file:
        outputList = []
        for eachLine in input_file:
            if eachLine == "\n": continue
            lineParts = eachLine.split("||")
            tempDict = {u"text:": lineParts[0], u"classes": [lineParts[1].rstrip()]}
            outputList.append(tempDict)

        with open(OUTPUT_FILE, 'w') as output_file:
            output = json.dumps(outputList, indent= 2, separators=(',', ': '))
            output_file.write(output)