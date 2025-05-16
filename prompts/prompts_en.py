# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

prompts_en = {
  'ASSOCIATION': {
    'WITH_BOTH_DESCRIPTIONS': "Tell me if you find a direct or indirect relationship between '{term}', which's description is '{term_description}', and '{associative_term}', which's description is '{associative_term_description}'.",
    'WITH_TERM_DESCRIPTION': "Tell me if you find a direct or indirect relationship between '{term}', which's description is '{term_description}', and '{associative_term}'.",
    'WITH_ASSOCIATIVE_TERM_DESCRIPTION': "Tell me if you find a direct or indirect relationship between '{term}' and '{associative_term}', which's description is '{associative_term_description}'.",
    'WITHOUT_DESCRIPTIONS': "Tell me if you find a direct or indirect relationship between '{term}' and '{associative_term}'.",
    'COMMON_PART':  """
                    If there is any way to associate them, even if it is not very clear, it already means they are related.

                    Response must be in JSON format, following this example:
                    {{"term": "{term}", "associative_term": "{associative_term}", "relationship": true/false, "reason": "reason why there is or isn't relationship between {term} and {associative_term}"}}
                    """,
  },
  'GENERATION': {
    'WITH_ASSOCIATIVE_TERM': {
      'WITH_TERM_DESCRIPTION':  """
                                Generate {n} texts of less than {length} characters for a Google Ads ad.
                                This ad has to be related with the term '{term}', which's description is '{term_description}', and '{associative_term}'.
                                They must incentivize the reader to buy '{term}' because '{associative_term}' is trending.
                                Consider the following association reason between the two terms: '{association_reason}'.
                                Try to include key words related with the trending topic in the texts.
                                If the generated texts are long, try to include the retailer's name, which is {company}, in the texts.

                                Response must be in exactly the following format:
                                ["write here the text 1", "write here the text 2", ..., "write here the text {n}"]
                                The response must follow exactly that format. It does not have to contain any additional commas, whitespaces or line breaks. It must be just a comma-separated list of texts between square brackets and thats it.
                                """,
      'WITHOUT_RELATIONSHIP_AND_DESCRIPTIONS':  """
                                                Generate {n} texts of less than {length} characters for a Google Ads ad.
                                                This ad has to be related with the term '{term}' and '{associative_term}'.
                                                They must incentivize the reader to buy '{term}' because '{associative_term}' is trending.

                                                Response must be in exactly the following format:
                                                ["write here the text 1", "write here the text 2", ..., "write here the text {n}"]
                                                The response must follow exactly that format. It does not have to contain any additional commas, whitespaces or line breaks. It must be just a comma-separated list of texts between square brackets and thats it.
                                                """,
        'WITHOUT_DESCRIPTIONS': """
                                Generate {n} texts of less than {length} characters for a Google Ads ad.
                                This ad has to be related with the term '{term}' and '{associative_term}'.
                                They must incentivize the reader to buy '{term}' because '{associative_term}' is trending.
                                Consider the following association reason between the two terms: '{association_reason}'.
                                Try to include key words related with the trending topic in the texts.
                                If the generated texts are long, try to include the retailer's name, which is {company}, in the texts.

                                Response must be in exactly the following format:
                                ["write here the text 1", "write here the text 2", ..., "write here the text {n}"]
                                The response must follow exactly that format. It does not have to contain any additional commas, whitespaces or line breaks. It must be just a comma-separated list of texts between square brackets and thats it.
                                """,
            'WITH_ASSOCIATIVE_TERM_DESCRIPTION':  """
                                                  Generate {n} texts of less than {length} characters for a Google Ads ad.
                                                  This ad has to be related with the term '{term}' and '{associative_term}', which's description is '{associative_term_description}'.
                                                  They must incentivize the reader to buy '{term}' because '{associative_term}' is trending.
                                                  Consider the following association reason between the two terms: '{association_reason}'.
                                                  Try to include key words related with the trending topic in the texts.
                                                  If the generated texts are long, try to include the retailer's name, which is {company}, in the texts.

                                                  Response must be in exactly the following format:
                                                  ["write here the text 1", "write here the text 2", ..., "write here the text {n}"]
                                                  The response must follow exactly that format. It does not have to contain any additional commas, whitespaces or line breaks. It must be just a comma-separated list of texts between square brackets and thats it.
                                                  """,
            'WITH_BOTH_DESCRIPTIONS':   """
                                                  Generate {n} texts of less than {length} characters for a Google Ads ad.
                                                  This ad has to be related with the term '{term}', which's description is '{term_description}', and '{associative_term}', which's description is '{associative_term_description}'.
                                                  They must incentivize the reader to buy '{term}' because '{associative_term}' is trending.
                                                  Consider the following association reason between the two terms: '{association_reason}'.
                                                  Try to include key words related with the trending topic in the texts.
                                                  If the generated texts are long, try to include the retailer's name, which is {company}, in the texts.

                                                  Response must be in exactly the following format:
                                                  ["write here the text 1", "write here the text 2", ..., "write here the text {n}"]
                                                  The response must follow exactly that format. It does not have to contain any additional commas, whitespaces or line breaks. It must be just a comma-separated list of texts between square brackets and thats it.
                                        """
        },
        'WITHOUT_ASSOCIATIVE_TERM': {
            'WITH_DESCRIPTION': """
                                Generate {n} texts of less than {length} characters for a Google Ads ad.
                                This ad has to be related with the term '{term}', which's description is '{term_description}'.
                                The ad is from a company called '{company}' and must incentivize the reader to buy '{term}'.

                                Response must be in exactly the following format:
                                ["write here the text 1", "write here the text 2", ..., "write here the text {n}"]
                                The response must follow exactly that format. It does not have to contain any additional commas, whitespaces or line breaks. It must be just a comma-separated list of texts between square brackets and thats it.
                                """,
            'WITHOUT_DESCRIPTION':  """
                                    Generate {n} texts of less than {length} characters for a Google Ads ad.
                                    This ad has to be related with the term '{term}'.
                                    The ad is from a company called '{company}' and must incentivize the reader to buy '{term}'.

                                    Response must be in exactly the following format:
                                    ["write here the text 1", "write here the text 2", ..., "write here the text {n}"]
                                    The response must follow exactly that format. It does not have to contain any additional commas, whitespaces or line breaks. It must be just a comma-separated list of texts between square brackets and thats it.
                                    """,
        },
        'PATHS_WITH_TERM_DESCRIPTION': """
                                          I'll give you a term and its description, and you must obtain a URL path divided in {n} pieces for that term.
                                          The URL path must refer to the term '{term}' and to its description '{term_description}'.
                                          Each part of the path must be extremely short, just one single word that refers to the idea of '{term}' and its description '{term_description}'.
                                          For example, if the term is 'Samsung Galaxy S23 Ultra' and its description is 'Telefono Samsung Galaxy S23 Ultra, el buque insignia de Samsung para la gama alta con pantalla super amoled y camara de altisima calidad', the first part of the path can be 'phones' and the second part of the path can be 'galaxy'.
                                          This URL path will be used in an ecommerce site like this: www.ecommerce.com/PATH1/PATH2. Another example: www.ecommerce.com/zapatillas/nike-running
                                          The first part of the path must be a category and the second part of the path something a little bit more specific.
                                          Some examples for you to inspire: 'shoes/nike-running', 'tvs/samsung', 'trucks/ford-ranger'/
                                          IMPORTANT: it MUST NOT contain caps letters nor spaces.

                                          Response must be in exactly the following format:
                                          ["write here the first part of the path", "write here the second part of the path"]
                                          The response must follow exactly that format. It does not have to contain any additional commas, whitespaces or line breaks. It must be just a comma-separated list of texts between square brackets and thats it.
                                          """,
        'PATHS_WITHOUT_TERM_DESCRIPTION':  """
                                          I'll give you a term and you must obtain a URL path divided in {n} pieces for that term.
                                          The URL path must refer to the term '{term}' .
                                          Each part of the path must be extremely short, just one single word that refers to the idea of '{term}'.
                                          For example, if the term is 'Samsung Galaxy S23 Ultra' and its description is 'Telefono Samsung Galaxy S23 Ultra, el buque insignia de Samsung para la gama alta con pantalla super amoled y camara de altisima calidad', the first part of the path can be 'phones' and the second part of the path can be 'galaxy'.
                                          This URL path will be used in an ecommerce site like this: www.ecommerce.com/PATH1/PATH2. Another example: www.ecommerce.com/zapatillas/nike-running
                                          The first part of the path must be a category and the second part of the path something a little bit more specific.
                                          Some examples for you to inspire: 'shoes/nike-running', 'tvs/samsung', 'trucks/ford-ranger'/
                                          IMPORTANT: it MUST NOT contain caps letters nor spaces.

                                          Response must be in exactly the following format:
                                          ["write here the first part of the path", "write here the second part of the path"]
                                          The response must follow exactly that format. It does not have to contain any additional commas, whitespaces or line breaks. It must be just a comma-separated list of texts between square brackets and thats it.
                                        """,
    'KEYWORDS': """
                Give me a list of up to 10 keywords for a Google Ads ad related to the term '{term}'.
                Response must be in exactly the following format:
                ["Keyword 1", "Keyword 2", ..., "Keyword N"]
                Do not add line breaks or unnecessary spaces, just give me the comma-separated keyword list.
                """

  },
  'SIZE_ENFORCEMENT': """
                    I will give you one text for a Google Ads ad that is too long.
                    Make it shorter, it has to be shorter than {max_length} characters.
                    The text is: {copy}

                    Give me the response like this:
                    shortened_text
                    Just give me as a response the shortened text without quotation marks, line breaks or anything else.
                    """
}