import numpy as np

class MarkovModel:
    def __init__(self, k):
        """
        Initialize a Markov model with a particular prefix length
        
        Parameters
        ----------
        k: int
            Length of prefix to use
        """
        self.k = k
        ## TODO: Setup any other member variables that might be useful
        self.chars = set([])
        self.map = dict()
        
    
    def load_file(self, filename):
        """
        Load in an entire file as one string and add
        it to the model

        Parameters
        ----------
        filename: string
            Path to file to load
        """
        fin = open(filename)
        self.add_string(fin.read())
        fin.close()
    
    def load_file_lines(self, filename):
        """
        Load in an entire file as one string and add
        it to the model

        Parameters
        ----------
        filename: string
            Path to file to load
        """
        fin = open(filename, encoding='utf-8')
        for line in fin.readlines():
            line = line.rstrip()
            if len(line) > 0:
                self.add_string(line)
        fin.close()
    
    def add_string(self, s):
        """
        Incorporate a particular string into your model by adding any prefixes
        if they don't exist and by updating counts
        """
        ## TODO: Fill this in
        if len(s) >= self.k:
            c = s + s[0:self.k]
            for i in range(len(s)):
                prefix = c[i:i+self.k]
                post = c[i+self.k]
                if not post in self.chars:
                    self.chars.add(post)
                if not prefix in self.map:   
                    self.map[prefix] = dict()
                if not post  in self.map[prefix]:
                    self.map[prefix][post] = 0
                self.map[prefix][post] += 1
                
        return # This does nothing
    
    def get_log_probability(self, s):
        """
        Compute the log probability of a particular string according to the model

        Parameters
        ----------
        s: string
            String for which to compute the probability
        
        Returns
        -------
        float: Log probability
        """
        log_prob = 0
        ## TODO: Fill this in
        if len(s) >= self.k:
            N = len(self.chars)
            for i in range(len(s)-self.k):
                prefix = s[i:i+self.k]
                post = s[i+self.k]
                
                num_prefix = 0
                num_next = 0
            
                if prefix in self.map:
                    for k,v in self.map[prefix].items():
                        num_prefix += v
                        if post == k:
                            num_next = v        
                log_prob += np.log((num_next + 1)/(num_prefix + N))            
                 
        return log_prob

    def synthesize_text(self, length):
        import random
        """
        Synthesize random text of a particular length in the style captured
        by this model

        Parameters
        ----------
        length: int
            How many characters are in the string to synthesize
        
        Returns
        -------
        string: The synthesized text
        """
        ## TODO: Fill this in
        prefixes = list()
        counts = list()
        
        for k, v in self.map.items():
            prefixes.append(k)
            counts.append(sum(v.values()))
            
        
        # start the word with the prefix
        synth_text = random.choices(population = prefixes,
                                   weights=counts)[0]
        
        for i in range(length-self.k):
            prefix = synth_text[-self.k:]
            post = random.choices(population=list(self.map[prefix].keys()),
                                 weights=list(self.map[prefix].values())
                                 )[0]
            synth_text += post
            
        
        return synth_text # This does nothing