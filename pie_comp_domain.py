import sys
import csv

# dedupe function if the customer wants it in the future. 
def dedupe_file(input_file):
    data = [row for row in input_file]
    deduped = list(set(data))
    return deduped


def pie_comp_domain(input_file, comp_file, out_file):
    # read in client_ID's/domains file
    delim_type = '\t'
    data = csv.reader(input_file, delimiter=str(delim_type))
    data = [row for row in data]
    # populate dictionary of client_ID'ss/domains
    dict_clientId = {}
    for e in data:
        if e[0] in dict_clientId:
            dict_clientId[e[0]].append(e[1])
        else:
            dict_clientId[e[0]] = [e[1]]
    # read in company/client_ID file
    comp_delim = '|'
    #comp_in = dedupe_file(comp_file)
    #print comp_in
    comps = csv.reader(comp_file, delimiter=str(comp_delim))
    comps = [row for row in comps]
    # create csv writer object
    writer = csv.writer(out_file, quoting=csv.QUOTE_ALL)
    new_line = []
    # iterate through list of companies/Client_id's
    for comp in comps:
        #print(comp)
        # append "None" to blank Client_ID's 
        if comp[1] == '':
            writer.writerow([comp[0],"None"])
        # append "None" to non Client_ID matches
        elif comp[1] not in dict_clientId:
            writer.writerow([comp[0],"None"])
        else:
            # create list of company name plus domaind for matches
            new_line = [comp[0]]
            for v in dict_clientId[comp[1]]:
                new_line.append(v)
            writer.writerow(new_line)
        new_line = []



def strip_suffix(name):  #strip suffix to create output file name w/'.csv'
    return name[:-4]

file_ext = '.append.csv'

# get script path
script_path = os.path.dirname(os.path.abspath(__file__))

# # import file
# this is the client_id and domain file
try:
    file_name = sys.argv[1]
except:
    sys.exit('ERROR: missing FILENAME file. \n example: C:>python pie_comp_domain.py FILENAME LAYOUT [-t,-p] \n optional -t for tab, -p for pipe. defaults to comma delimited')
#file_name = sys.argv[1]
in_file = script_path + '\\' + file_name

# this is the company name and client_id file
try:
    comp_file_name = sys.argv[2]
except:
    sys.exit('ERROR: missing FILENAME file. \n example: C:>python pie_comp_domain.py FILENAME LAYOUT [-t,-p] \n optional -t for tab, -p for pipe. defaults to comma delimited')
#comp_file_name = sys.argv[1]
co_file = script_path + '\\' + comp_file_name
# in_file = "Symantec domestic_020915.csv"
# co_file = "Symantec domestic 020915 comps.Txt"
with open(in_file, 'r') as input_file, open(co_file, 'r') as comp_file, open(strip_suffix(co_file) + file_ext, 'w', newline="") as out_file:
                pie_comp_domain(input_file, comp_file, out_file)


