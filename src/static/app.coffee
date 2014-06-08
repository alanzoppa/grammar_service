window.pos_tags = {
  'CC': {
    description: "Coordinating conjunction",
    class: "coordinating-conjunction"
  },
  'CD': {
    description: "Cardinal number",
    class: "cardinal-number"
  },
  'DT': {
    description: "Determiner",
    class: "determiner"
  },
  'EX': {
    description: "Existential there",
    class: "existential-there"
  },
  'FW': {
    description: "Foreign word",
    class: "foreign-word"
    type: 'noun-type'
  },
  'IN': {
    description: "Preposition or subordinating conjunction",
    class: "preposition-or-subordinating-conjunction"
    type: 'minor-type'
  },
  'JJ': {
    description: "Adjective",
    class: "adjective"
    type: 'adj-type'
  },
  'JJR': {
    description: "Adjective, comparative",
    class: "adjective-or-comparative"
    type: 'adj-type'
  },
  'JJS': {
    description: "Adjective, superlative",
    class: "adjective-or-superlative"
    type: 'adj-type'
  },
  'LS': {
    description: "List item marker",
    class: "list-item-marker"
  },
  'MD': {
    description: "Modal",
    class: "modal"
  },
  'NN': {
    description: "Noun, singular or mass",
    class: "noun-or-singular-or-mass"
    type: 'noun-type'
    importance: 1
  },
  'NNS': {
    description: "Noun, plural",
    class: "noun-or-plural"
    type: 'noun-type'
    importance: 3
  },
  'NNP': {
    description: "Proper noun, singular",
    class: "proper-noun-or-singular"
    type: 'noun-type'
    importance: 0
  },
  'NNPS': {
    description: "Proper noun, plural",
    class: "proper-noun-or-plural"
    type: 'noun-type'
    importance: 0
  },
  'PDT': {
    description: "Predeterminer",
    class: "predeterminer"
    type: 'noun-type'
  },
  'POS': {
    description: "Possessive ending",
    class: "possessive-ending"
    type: 'noun-type'
  },
  'PRP': {
    description: "Personal pronoun",
    class: "personal-pronoun"
    type: 'noun-type'
    importance: 3
  },
  'PRP$': {
    description: "Possessive pronoun",
    class: 'possessive-pronoun'
    type: 'noun-type'
    importance: 3
  },
  'RB': {
    description: "Adverb",
    class: "adverb"
    type: 'adverb-type'
  },
  'RBR': {
    description: "Adverb, comparative",
    class: "adverb-or-comparative"
    type: 'adverb-type'
  },
  'RBS': {
    description: "Adverb, superlative",
    class: "adverb-or-superlative"
    type: 'adverb-type'
  },
  'RP': {
    description: "Particle",
    class: "particle"
    like_previous: true
  },
  'SYM': {
    description: "Symbol",
    class: "symbol"
  },
  'TO': {
    description: "to",
    class: "to"
  },
  'UH': {
    description: "Interjection",
    class: "interjection"
  },
  'VB': {
    description: "Verb, base form",
    class: "verb-or-base-form"
    type: 'verb-type'
  },
  'VBD': {
    description: "Verb, past tense",
    class: "verb-or-past-tense"
    type: 'verb-type'
  },
  'VBG': {
    description: "Verb, gerund or present participle",
    class: "verb-or-gerund-or-present-participle"
    type: 'verb-type'
    importance: 2;
  },
  'VBN': {
    description: "Verb, past participle",
    class: "verb-or-past-participle"
    type: 'verb-type'
  },
  'VBP': {
    description: "Verb, non-3rd person singular present",
    class: "verb-or-non-3rd-person-singular-present"
    type: 'verb-type'
  },
  'VBZ': {
    description: "Verb, 3rd person singular present",
    class: "verb-or-3rd-person-singular-present"
    type: 'verb-type'
    importance: 5
  },
  'WDT': {
    description: "Wh-determiner",
    class: "wh-determiner"
  },
  'WP': {
    description: "Wh-pronoun",
    class: "wh-pronoun"
    type: 'noun-type'
    importance: 4
  },
  'WP$': {
    description: "Possessive wh-pronoun",
    class: 'possessive-wh-pronoun'
  },
  'WRB': {
    description: "Wh-adverb",
    class: "wh-adverb"
  }
}

sample_text = "\nIn a Mr. Lee's Greater Hong Kong franchise on the outskirts of Phoenix, Rat Thing number B-782 comes awake.\n\nFido is waking up because the dogs are barking tonight.\n\nThere is always barking. Much of the barking is very far away. Fido knows that faraway barks are not as important as close barks, and so he often sleeps through these.\n\nBut sometimes a faraway bark will carry a special sound that makes Fido excited, and he can't help waking up.\n\nHe is hearing one of those barks right now. It comes from far away but it is urgent. Some nice doggie somewhere is very upset. He is so upset that his barking has spread to all the other doggies in the pack.\n\nFido listens to the bark. He gets excited, too. Some bad strangers have just been very close to a nice doggie's yard. They were in a flying thing. They had lots of guns.\n\nFido doesn't like guns very much. A stranger with a gun shot him once and made him hurt. Then the nice girl came and helped him.\n\nThese are extremely bad strangers. Any nice doggie in his right mind would want to hurt them and make them go away. As Fido listens to the bark, he sees what they look like and hears the way they sound. If any of these very bad strangers ever come into his yard, he will be extremely upset.\n\nThen Fido notices that the bad strangers are chasing someone. He can tell they are hurting her by the way her voice sounds and the way she moves.\n\nThe bad strangers are hurting the nice girl who loves him!\n\nFido gets more angry than he has ever been, even more angry than when a bad man shot him long ago.\n\nHis job is to keep bad strangers out of his yard. He does not do anything else. But it's even more important to protect the nice girl who loves him. That is more important than anything. And nothing can stop him. Not even the fence.\n\nThe fence is very tall. But he can remember a long time ago when he used to jump over things that were taller than his head.\n\nFido comes out of his doggie house, curls his long legs beneath him, and jumps over the fence around his yard before he has remembered that he is not capable of jumping over it. This contradiction is lost on him, though; as a dog, introspection is not one of his strong points.\n\nThe bark is spreading to another place far away. All the nice doggies who live in this faraway place are being warned to look out for the very bad strangers and the girl who loves Fido, because they are going to that place. Fido sees the place in his mind. It is big and wide and flat and open, like a nice field for chasing Frisbees. It has lots of big flying things. Around the edges are a couple of yards where nice doggies live.\n\nFido can hear those nice doggies barking in reply. He knows where they are. Far away. But you can get there by streets. Fido knows a whole lot of different streets. He just runs down streets, and he knows where he is and where he's going.\n\nAt first, the only trace that B-782 leaves of his passage is a dancing trail of sparks down the center of the franchise ghetto. But once he makes his way out onto a long straight piece of highway, he begins to leave further evidence: a spume of shattered blue safety glass spraying outward in parallel vanes from all four lanes of traffic as the windows and the windshields of the cars blow out of their frames, spraying into the air like rooster tails behind a speedboat.\n\nAs part of Mr. Lee's good neighbor policy, all Rat Things are programmed never to break the sound barrier in a populated area. But Fido's in too much of a hurry to worry about the good neighbor policy. Jack the sound barrier. Bring the noise.\n\n"

punctuation_chars = ['.', ',', ';', '!', '?', 'n\'t']

class Document
  constructor: (document)->
    @paragraphs = (new Paragraph(paragraph) for paragraph in document)
  print: ->
    $('<div/>').append((paragraph.print() for paragraph in @paragraphs))[0].innerHTML


class Paragraph
  constructor: (paragraph)->
    @sentences = (new Sentence(sentence) for sentence in paragraph)
  print: ->
    paragraph = []
    for sentence,i in @sentences
      paragraph.push(sentence.print())
      unless i+1 == @sentences.length 
        paragraph.push ' '
    $('<p/>').append paragraph


class Sentence
  constructor: (sentence)->
    @words = (new Word(word) for word in sentence)
  print: ->
    sentence = []
    for word, i in @words
      nextWord = @words[i+1]
      sentence.push word.print()
      unless (nextWord?.text in punctuation_chars) or nextWord?.class is 'possessive-ending'
        sentence.push ' '
    $('<span>', {class: 'sentence'}).append(sentence)

class Word
  constructor: (word)->
    [@text, @pos] = word
    tag = pos_tags[@pos]
    @class = tag?.class
    @title = tag?.description
    if tag?.type
      @class += " #{tag.type}"
    if tag?.importance?
      @class += " importance-#{tag.importance}"

  print: ->
    $('<span/>', class: @class, title: @title).text(@text)

# The key needs to match your method's input parameter (case-sensitive).
$.ajax(
  type: "POST"
  url: "/"
  data: JSON.stringify(documents: [sample_text])
  contentType: "application/json; charset=utf-8"
  dataType: "json"
).success (response, status, promise) ->
  for document in response.documents
    doc = new Document document
    window.doc = doc
    $('#text-highlighted').html(doc.print())
  return

