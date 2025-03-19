import json
class DFA:
    def __init__(self, states, alphabet, start_state, accept_states, transitions, test_string):
        self.states = states
        self.alphabet = alphabet
        self.start_state = start_state
        self.accept_states = accept_states
        self.transitions = transitions
        self.test_string = test_string
    def run_dfa(self):
        path = ["q0"]
        i = 0
        current_state = self.start_state
        while i < len(self.test_string):
            c = self.test_string[i]
            if c not in self.alphabet:
                # should not actually happpen if the json is correct
                break
            current_state = self.transitions[current_state][c]
            path.append(current_state)
            i += 1
        return path
    def print_result(self):
        path = self.run_dfa()
        path_str = "Path: "
        for i,state in enumerate(path):
            path_str += state
            if i < len(path) - 1:
                path_str += " -> "
        print(path_str)
        if path[-1] in self.accept_states:
            print('Status: ACCEPTED')
        else:
            print('Status: REJECTED')
class DFA_json_reader:
    def convert_json_to_dict(file_path):
        with open(file_path) as json_file:
            data = json.load(json_file)
        return data
    def convert_dict_to_dfa_class(data):
        return DFA(data['states'], data['alphabet'], data['start_state'], data['accept_states'], data['transitions'], data['test_string'])
    def convert_data_to_dict(data):
        data = {"states": data.states, "alphabet": data.alphabet, "start_state" : data.start_state, 
                "accept_states": data.accept_states, "transitions": data.transitions, "test_string": data.test_string}
        return data
    def convert_dict_to_json(data, file_path):
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
  #If we want to directly create JSON from the program
'''
data1 = DFA(['q0', 'q1', 'q2', 'q3'], ['a', 'b'], 'q0', ['q2','q3'],{
            "q0": { "a": "q1", "b": "q3" },"q1": { "a": "q1", "b": "q2" },
            "q2": { "a": "q1", "b": "q3" }, "q3": { "a": "q2", "b": "q3" }}, 'aa')
data_dict = DFA_json_reader.convert_data_to_dict(data1)
DFA_json_reader.convert_dict_to_json(data_dict, 'data.json')
'''
example_1 = DFA_json_reader.convert_json_to_dict('data_1.json')
example_2 = DFA_json_reader.convert_json_to_dict('data_2.json')
dfa_1 = DFA_json_reader.convert_dict_to_dfa_class(example_1)
dfa_1.print_result() 
dfa_2 = DFA_json_reader.convert_dict_to_dfa_class(example_2)
dfa_2.print_result()