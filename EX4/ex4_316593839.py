''' Exercise #4. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def second_most_popular_character(my_string):
    dic = {}
    for x in my_string:
        if str(x) not in dic:
            dic['{}'.format(x)] = my_string.count(x)
    i = sorted(dic.items())
    k = sorted(dic.keys())
    max1 = max(dic.values())
    max2 = 0
    max2key = ''
    for key, value in i:
        if value > max2 and value < max1:
            max2 = value
            max2key = str(key)
    if max2 == 0:
        return k[0]
    return max2key

#########################################
# Question 2 - do not delete this comment
#########################################
def diff_sparse_matrices(lst):
    base_matrix = lst[0]
    for i in range(1, len(lst)):
        for key, value in lst[i].items():
            if key in base_matrix.keys():
                base_matrix[key] = base_matrix[key] - value
            else:
                base_matrix[key] = - value

    remove = [k for k in base_matrix if base_matrix[k] == 0]
    for k in remove:
        del base_matrix[k]

    return base_matrix


#########################################
# Question 3 - do not delete this comment
#########################################
def find_substring_locations(s, k):
    dic = {}
    lst1 = []
    for i in range(len(s) - k + 1):
        per = s[i:i + k]
        lst1.append(per)
        if per not in dic:
            dic[per] = []
    for i, cop in enumerate(lst1):
        if cop in dic:
            dic[cop].append(i)
    return dic


#########################################
# Question 4 - do not delete this comment
#########################################
def count_lines(in_file, out_file):
    f = open(in_file, 'r')
    r = f.readlines()
    f.close()
    counter = 0
    for line in r:
        counter += 1
    f1 = open(out_file, 'w')
    f1.write(str(counter))
    f1.close()

#########################################
# Question 5 - do not delete this comment
#########################################
def simple_sent_analysis(in_file):
    dir = {'happy': 0, 'sad': 0}
    try:
        f = open(in_file, 'r')
        r = f.read()
        spl = r.split(' ')
        extra = [',', '?', '-', ';', '%', '!']
        for i, x in enumerate(spl):
            if '\n' in x:
                y = spl.pop(i).split('\n')
                for letter in y:
                    spl.append(letter)
        for i, x in enumerate(spl):
            for ex in extra:
                if x[0] == ex or x[-1] == ex and not x == ex:
                    spl[i] = spl[i].strip(ex)
        for let in spl:
            if let.lower() in dir:
                dir[let.lower()] += 1
        f.close()
        return dir
    except Exception as e:
        counter = in_file.count('/')
        c = [c for c in in_file.split('/')]
        print(f'Cannot encode {c[counter]} due to IO error')
        f.close()
        return {}


#########################################
# Question 6 - do not delete this comment
#########################################
def calc_profit_per_group(in_file):
    try:
        with open(in_file) as scvFile:
            reader = scvFile.readlines()
            dic = {}
            happy = 0
            happy_count = 0
            sad = 0
            sad_count = 0
            neutral = 0
            neutral_count = 0
            more_then_one = []
            x = [line.split(',') for line in reader]
            for row in x:
                try:
                    float(row[1])
                except Exception as e:
                    return 'ValueError: Invalid input'
                if len(row) != 3 or row[2].strip('\n') not in ['happy', 'sad', 'neutral']:
                    raise ValueError('Invalid input')
                if row[0] not in dic.keys():
                    dic[row[0]] = {'amount': float(row[1]), 'status': row[2]}
                else:
                    more_then_one.append(row[0])
            if len(more_then_one) > 0:
                raise ValueError('Double')
            dic_out = {'happy': 0, 'sad': 0, 'neutral': 0}
            for x in dic.values():
                if x['status'].strip('\n') == 'happy':
                    dic_out['happy'] = dic_out['happy'] + x['amount']
                    happy_count += 1
                elif x['status'].strip('\n') == 'sad':
                    dic_out['sad'] = dic_out['sad'] + x['amount']
                    sad_count += 1
                elif x['status'].strip('\n') == 'neutral':
                    dic_out['neutral'] = dic_out['neutral'] + x['amount']
                    neutral_count += 1
            change = [k for k in dic_out if dic_out[k] == 0]
            for k in change:
                dic_out[k] = 'NA'
            for key in dic_out:
                if dic_out[key] != 'NA':
                    if key == 'happy':
                        dic_out[key] = dic_out[key] / happy_count
                    elif key == 'sad':
                        dic_out[key] = dic_out[key] / sad_count
                    elif key == 'neutral':
                        dic_out[key] = dic_out[key] / neutral_count
            scvFile.close()
            return dic_out
    except Exception as e:
        if str(e) == 'Invalid input':
            scvFile.close()
            return 'ValueError: ' + str(e)
        elif str(e) == 'Double':
            scvFile.close()
            return f'The series {more_then_one[0]}_name appears more than once.'
        else:
            counter = in_file.count('/')
            c = [c for c in in_file.split('/')]
            return f' encode {c[counter]} due to IO error'

#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################

# ============================== END OF FILE =================================
