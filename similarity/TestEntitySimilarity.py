from sematch.semantic.similarity import EntitySimilarity
entity_sim = EntitySimilarity()

sherlock = 'http://dbpedia.org/resource/Sherlock_Holmes'
benjamin = 'http://dbpedia.org/resource/Benjamin_Franklin'
charles = 'http://dbpedia.org/resource/Charles_Dickens'
arthur = 'http://dbpedia.org/resource/Arthur_Conan_Doyle'
steve = 'http://dbpedia.org/resource/Steve_Jobs'
apple = 'http://dbpedia.org/resource/Apple_Inc.'

print(entity_sim.similarity(sherlock, arthur))