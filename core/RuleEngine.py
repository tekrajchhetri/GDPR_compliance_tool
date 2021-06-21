# -*- coding: utf-8 -*-
# @Time    : 21.06.21 10:26
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : RuleEngine.py
# @Software: PyCharm
import re
import spacy

class RuleEngine:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_trf')

    def trim_and_lower(self, input_string):
        return input_string.lower().strip()

    def remove_punct(self, input_string):
        return re.sub(r'[^\w\s]', '', self.trim_and_lower(input_string))

    def remove_stop_words(self, input_string):
        doc = self.nlp(input_string)
        return " ".join([w.text for w in doc if not w.is_stop])

    def full_match_ptext(self, purpose_from_consent_doc, purpose_from_dpc):
        return self.trim_and_lower(purpose_from_consent_doc) == self.trim_and_lower(purpose_from_dpc)