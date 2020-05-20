
## About Naki

![Naki](http://turing.iimas.unam.mx/wix/static/img/banner.jpg "NLP for our languages")


This page tries to assemble all the research on Natural Language Processing (NLP) for native and indigenous languages of the American continent. Our languages are in danger, especially if they don't get involved in the new digital boom, that is introduced even into the most remote communities. Nevertheless, scientific and engineering work has been done in the field, much more work is necessary to archive usable tools that can compete with the products from the big companies (as Google Translate, Alexa, etc.).  To push forward this effort,  this work wants to generate an (as much as possible) complete list.

Our main aim is to encourage native speakers, researchers, and engineers to participate in this effort. Hopefully, we can do it with these survey.

If you want more information, please read our paper: ["Challenges of language technologies for the indigenous languages of the Americas"](http://aclweb.org/anthology/C18-1006). We also invite you to have a look at our [presentation](https://github.com/pywirrarika/naki/blob/master/challenges-slides.pdf)

**Last Update:** 23/March/2020

# Table of Contents
1. [Machine Translation](#machine-translation)
2. [Automatic Lexical extraction](#automatic-lexical-extraction)
3. [Morphologcal analysis and segmentation](#morphologcal-analysis-and-segmentation)
4. [Corpus and digital resources](#corpus-and-digital-resources)
5. [Speech Recognition](#speech-recognition)
6. [POS Tagging](#pos-tagging)
7. [Parsing](#parsing)
8. [OCR](#ocr)
9. [Spell checking](#spell-checking)
10. [WordNet](#wordnet)
11. [Language ID](#language-id)
12. [Code-Switching and Multilingual NLP](#code-switching-and-multilingual-nlp)
13. [Tools, documentation and education](#tools-documentation-and-education)
14. [Computational Linguistic Analyze and Surveys](#computational-linguistic-analyze-and-surveys)
15. [Contact](#contact)


## Corpus and digital resources

**Online Corpus Resources**
- [BriBri Anotated speech + morphology corpus](http://www.bribri.net/)
- [Inukitut Morhological Database](http://www.inuktitutcomputing.ca/DataBase/info.php)
- [JW300](http://zeljkoagic.github.io/jw300/) Multilingual corpus that also include many indigenous languages of the american contienent.  ( Soon available at [OPUS](http://opus.nlpl.eu/) )
- [English-Inuktitut Parallel Corpus](http://www.inuktitutcomputing.ca/NunavutHansard/en/index-VX.html)
- [Nahuatl-Spanish, Axolot](http://www.corpus.unam.mx/axolotl/) Parallel Nahuatl - Spanish
- [Gran diccionario Nahuatl](http://www.gdn.unam.mx/)
- [Wixarika-Spanish](https://github.com/pywirrarika/wixarika-spanish) Parallel Wixarika - Spanish
- [Shipibo-Konibo Spanish](http://chana.inf.pucp.edu.pe/resources/parallel-corpus/) Parallel corpus.
- [Shipibo-Konibo Wordnet](http://chana.inf.pucp.edu.pe/resources/wordnet-shp/)
- [Shipibo-Konibo Lemma corpus](http://chana.inf.pucp.edu.pe/resources/lemma-pos/lemmatizer/)
- [Shipibo-Konbio POS-tag corpus](http://chana.inf.pucp.edu.pe/resources/lemma-pos/pos-tagger/)
- [Morphological reinflection (Navajo, Haida and Quechua)](https://github.com/sigmorphon/conll2017/tree/master/all)
- [Morpholigucal inflection SIGMPRPHON 2020 (Tlatepuzco Chinantec, San Pedro Amuzgo Amuzgos, Yoloxóchitl Mixtec, Chichicapan Zapotec, Yaitepec Chatino, Zenzontepec Chatino, Eastern Highland Chatino, Eastern Highland Otomi, Mezquital Otomi and Chichimec)](https://sigmorphon.github.io/sharedtasks/2020/task0/)
- [Siminchikkunarayku](https://siminchikkunarayku.pe/) A Speech Corpus for Preservation of Southern Quechua
- [Tsunkua](https://tsunkua.elotl.mx/about) Spanish-Hñahñu (Otomi) parallel corpus.
- [Universal Dependencies](https://universaldependencies.org/): Mbya Guarani, Shipibo Konibo, Cusco Quechua
- [FastText](https://fasttext.cc/docs/en/crawl-vectors.html): Nahuatl

**Scientific papers**

- Frey, B. (2020). [“Data is nice:” Theoretical and pedagogical implications of an Eastern Cherokee corpus](https://scholarspace.manoa.hawaii.edu/bitstream/10125/66556/ldc-sp20-frey.pdf). LD&C Special Publication.

- Duan, M., Fasola, C., Rallabandi, S. K., Vega, R. M., Anastasopoulos, A., Levin, L., & Black, A. W. (2019). [A Resource for Computational Experiments on Mapudungun](https://arxiv.org/abs/1912.01772). arXiv preprint arXiv:1912.01772.

- Agić, Ž., & Vulić, I. (2019, July). [JW300: A Wide-Coverage Parallel Corpus for Low-Resource Languages](https://www.aclweb.org/anthology/P19-1310/). In Proceedings of the 57th Conference of the Association for Computational Linguistics (pp. 3204-3210).

- Cynthia Montano, Gerardo Sierra, Gemma Bel-Enguix & Helena Gomez-Adorno (2019). [A Mixtec-Spanish Parallel Corpus](http://www.winlp.org/wp-content/uploads/2019/final_papers/198_Paper.pdf). WiNLP 2019 Workshop, Florence, Italy.

- Ronald Cardenas, Rodolfo Zevallos,Reynaldo Baquerizo & Luis Camacho (2018) [Siminchik: A Speech Corpus for Preservation of Southern Quechua](http://lrec-conf.org/workshops/lrec2018/W14/pdf/4_W14.pdf). Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018), Miyazaki, Japan.

- Katherine M. Schmirler, Antti Arppe, Atticus G. Harrigan & Antti Arppe. (2017). [A Morphologically Tagged Corpus for Plains Cree](https://altlab.artsrn.ualberta.ca/wp-content/uploads/2017/09/PWOLL_2017.pdf). 4th Prairie Workshop on Language and Linguistics, University of Saskatchewan, March 18, 2017.

- Kazeminejad, G., Cowell, A., & Hulden, M. (2017). [Creating lexical resources for polysynthetic languages—the case of Arapaho](http://www.aclweb.org/anthology/W/W17/W17-0102.pdf). ComputEL-2, 10. (_Arapaho_)

- Cavar, M., Cavar, D., & Cruz, H. (2016). [Endangered Language Documentation: Bootstrapping a Chatino Speech Corpus, Forced Aligner](https://pdfs.semanticscholar.org/fa97/76c0deb92124497893fdf6e089ca5165bf57.pdf), ASR. In LREC.

- Bell, L., & Bell, L. (2017). [Work With What You’ve Got](http://www.aclweb.org/anthology/W/W17/W17-0107.pdf). ComputEL-2, 48. (_haida_)

- Galarreta Asian, A. P. (2017). [Generación de corpus paralelos para la implementación de un traductor automático estadístico entre shipibo-konibo y español](http://tesis.pucp.edu.pe/repositorio/handle/123456789/8325). Pontificia Universidad Católica del Perú.

- Gutierrez-Vasques, X., Sierra, G., & Pompa, I. H. (2016). [Axolotl: a Web Accessible Parallel Corpus for Spanish-Nahuatl](http://www.lrec-conf.org/proceedings/lrec2016/pdf/1068_Paper.pdf). In _LREC_.

- Hoenen, A. (2016). [Wikipedia Titles As Noun Tag Predictors](http://www.lrec-conf.org/proceedings/lrec2016/pdf/18_Paper.pdf). In LREC.

- Christodouloupoulos, C., & Steedman, M. (2015). [A massively parallel corpus: the Bible in 100 languages. Language resources and evaluation](http://link.springer.com/article/10.1007/s10579-014-9287-y), 49(2), 375-395.

- Goldhahn, D., Eckart, T., & Quasthoff, U. (2012). [Building Large Monolingual Dictionaries at the Leipzig Corpora Collection: From 100 to 200 Languages](https://pdfs.semanticscholar.org/1b56/0f892432fb853d233c92f9294640bc91de3c.pdf). In LREC (pp. 759-765).

- Rios, A., Göhring, A., & Volk, M. (2008). [A Quechua-Spanish parallel treebank](https://dspace.library.uu.nl/bitstream/handle/1874/296798/bookpart.pdf). LOT Occasional Series, 12, 53-64.

- Monson, C., Levin, L., Vega, R. M., Brown, R. D., Font-Llitjos, A., Lavie, A., ... & Huisca, R. (2004). [Data Collection and Analysis of Mapudungun Morphology for Spelling Correction.](http://repository.cmu.edu/cgi/viewcontent.cgi?article=1303&context=compsci) Computer Science Department, 300.

- Martin, J., Johnson, H., Farley, B., & Maclachlan, A. (2003). [Aligning and Using an English-Inuktitut Parallel Corpus](http://www.aclweb.org/anthology/W03-0320). In Proceedings of the HLT-NAACL 2003 Workshop on Building and Using Parallel Texts: Data Driven Machine Translation and Beyond.

## Machine Translation

**Online demos and software**
- [CHANA](http://chana.inf.pucp.edu.pe/index.php/en/home/) A software platform for automatic translation between Peruvian native languages
 - [Mainumby](http://plogs.soic.indiana.edu/mainumby/base) is an experimental translation app for the Guarani-Spanish language pair.
- [Microsoft Translator](https://www.microsoft.com/en-us/translator/languages.aspx) includes Yucatec Maya and Queretaro Otomí. 
- [Wayuu-Spanish Machine Translation](http://142.4.219.173/wt/) Author: José Cirilo González Hernández
- [Wixarika-Spanish Machine Translation](http://turing.iimas.unam.mx/wix/) Author: Jesús Manuel Mager Hois
- [Zapotec-Spanish Tranlsation APP](https://play.google.com/store/apps/details?id=com.SimplesoftMx.Didxazapp&hl=es). Author: Gonazlo Santiago Martínez. 


**Scientific papers**

- Gómez Montoya, H. E. (2019). [A crowd-powered conversational assistant for the improvement of a neural machine translation system in native peruvian language](http://tesis.pucp.edu.pe/repositorio/bitstream/handle/20.500.12404/14989/GOMEZ_MONTOYA_HECTOR_ERASMO_CROWD_POWERED_CONVERSATIONAL.pdf?sequence=1). Pontificia Universidad Católica del Perú.

- Gasser, M. (2018). [Mainumby: un Ayudante para la Traducci\'on Castellano-Guaran\'i](https://arxiv.org/abs/1810.08603v1). Xiv preprint arXiv:1810.08603.

- Mager, M., Mager, E., Medina-Urrea, A., Ruiz, I. V. M., & Kann, K. (2018). [Lost in Translation: Analysis of Information Loss During Machine Translation Between Polysynthetic and Fusional Languages](http://www.aclweb.org/anthology/W18-4808). In Proceedings of the Workshop on Computational Modeling of Polysynthetic Languages (pp. 73-83).

- Micher, J. (2018). [Using the Nunavut Hansard Data for Experiments in Morphological Analysis and Machine Translation](http://www.aclweb.org/anthology/W18-4807). In Proceedings of the Workshop on Computational Modeling of Polysynthetic Languages (pp. 65-72).

- Mager, M., & Meza, I. (2018). [Hacia la traducción automática de las lenguas indıgenas de méxico](https://dh2018.adho.org/hacia-la-traduccion-automatica-de-las-lenguas-indigenas-de-mexico/). In Proceedings of the 2018 Digital Humanities Conference. The Association of Digital Humanities Organizations.

- Huang, G., da Silva, T. F., Lamel, L., Gauvain, J. L., Gorin, A., Laurent, A., ... & Messouadi, A. (2017, March). [An investigation into language model data augmentation for low-resourced STT and KWS](ftp://tlp.limsi.fr/public/huang17.pdf). In 2017 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) (pp. 5790-5794). IEEE. (Guaraní)

- Galarreta, A. P., Melgar, A. & Ocevay, A. (September, 2017). [Corpus Creation and Initial SMT Experiments between Spanish and Shipibo-konibo](http://acl-bg.org/proceedings/2017/RANLP%202017/pdf/RANLP033.pdf). In RANLP 2017 (p. 238-244). 

- Mager Hois, Jesús Manuel. (2017). [Traductor híbrido wixárika - español con escasos recursos bilingües](http://code.kiutz.com/tesism/tesis.pdf). Universidad Autónoma Metropolitana. 

- Rios, A. (2016). [A basic language technology toolkit for Quechua](https://rua.ua.es/dspace/bitstream/10045/53566/1/PLN_56_10.pdf). 

- González Hernández, José C. (2016). [Herramienta de traduccin automática de wayuunaiki a español. Caso de estudio: sintagmas nominales y verbales simples](https://www.dropbox.com/s/kqfos49lw36oras/Trabajo%20Especial%20de%20Grado.pdf?dl=0). Universidad de Zulia. 

- Mager Hois, J. M., Barrón Romero, C., & Meza Ruiz, I. V. (2016). [Traductor estadístico wixarika-español usando descomposición morfológica](http://code.kiutz.com/arts/COMTEL2016.pdf). In COMTEL 2016.

- Coler M. and Homola Petr. (2014) [Ruble-based machine translation for Aymara](https://www.researchgate.net/publication/230785505_Rule-based_machine_translation_for_Aymara), in book Endangered Languages and New Technologies, Chapter: 4, Publisher: Cambridge University Press, Editors: Mari Jones, pp.67-80

- Uchamaco, G. R. L., Vilca, H. D. C., & Mariño, F. C. C. (2013). [Incubación de Sistema de Traducción Automática Español a Quechua, Basado en la Plataforma Libre y Código Abierto Apertium](http://journal.ceprosimad.com/index.php/ceprosimad/article/view/7/7). Ceprosimad, 2(1), 57-65.

- Fernández, D. I., Gamboa, O. Q., Atencia, J. M., & Bedoya, O. E. H. (2013, May). [Design and implementation of an “Web API” for the automatic translation Colombia's language pairs: Spanish-Wayuunaiki case.](https://www.researchgate.net/profile/Oscar_Bedoya4/publication/261093999_Design_and_implementation_of_an_Web_API_for_the_automatic_translation_Colombia%27s_language_pairs_Spanish-Wayuunaiki_case/links/57d019a108ae0c0081de9ea7/Design-and-implementation-of-an-Web-API-for-the-automatic-translation-Colombias-language-pairs-Spanish-Wayuunaiki-case.pdf) In Communications and Computing (COLCOM), 2013 IEEE Colombian Conference on (pp. 1-9). IEEE.

- Rudnick, A., & Gasser, M. (2013). [Lexical selection for hybrid mt with sequence labeling. In Proceedings of the Second Workshop on Hybrid Approaches to Translation](http://www.aclweb.org/anthology/W13-2815) (pp. 102-108).

- Vilca, Hugo David Calderon. (2009) [Traductor automático en línea del español al quechua, basado en la plataforma libre y código abierto Apertum. ](http://epg.unap.edu.pe/epgrd/investigacion/revistas/2009/7.pdf). Revista de Investigaciones (Puno)-Escuela de Posgrado de la UNA PUNO, vol. 5, no 3.

- Vilca, H. D. C. (2009). [Traductor automático en línea del español a quechua, basado en la plataforma libre y código abierto APERTIUM.](http://www.revistaepgunapuno.org/index.php/investigaciones/article/viewFile/24/18) Revista de Investigaciones (Puno)-Escuela de Posgrado de la UNA PUNO, 5(3).

- Castro Cavero, Indhira. (2007)[Traductor morfológico del castellano y quechua](https://app.tecsup.edu.pe/file/sga/documentos/revistaIi/Ii_1/6.pdf). Revista I+i, vol. 1, no. 1.

- Gasser, M. (2006). [Machine translation and the future of indigenous languages](http://homes.sice.indiana.edu/gasser/Papers/cilli.pdf). In I Congreso Internacional de Lenguas y Literaturas Indoamericanas, Temuco, Chile.

- Abdelali, A., Cowie, J., Helmreich, S., Jin, W., Milagros, M. P., Ogden, B., ... & Zacharski, R. (2006, August). [Guarani: a case study in resource development for quick ramp-up MT](https://s3.amazonaws.com/academia.edu.documents/30506035/amta-2006-abdelali.pdf?AWSAccessKeyId=AKIAIWOWYYGZ2Y53UL3A&Expires=1518600723&Signature=XX1k2XMaF8%2BRq6WxvBtCFbFv%2Fl4%3D&response-content-disposition=inline%3B%20filename%3DGuarani_a_case_study_in_resource_develop.pdf). In Proceedings of the 7th Conference of the Association for Machine Translation in the Americas,“Visions for the Future of Machine Translation (pp. 1-9).

- Monson, C., Llitjós, A. F., Aranovich, R., Levin, L., Brown, R., Peterson, E., ... & Lavie, A. (2006). [Building NLP systems for two resource-scarce indigenous languages: mapudungun and Quechua. Strategies for developing machine translation for minority languages](http://www.cs.cmu.edu/afs/cs.cmu.edu/project/cmt-40/OldFiles/OldFiles/Nice/Papers/esslli-06/ResourceScarceLanguageEngineeringWorkshop9.pdf), 15.

- Schafer, C., & Drábek, E. F. (2005, June). [Models for inuktitut-english word alignment](https://aclanthology.info/pdf/W/W05/W05-0811.pdf). In Proceedings of the acl workshop on building and using parallel texts (pp. 79-82). Association for Computational Linguistics.

- Langlais, P., Gotti, F., & Cao, G. (2005, June). [Nukti: English-inuktitut word alignment system description](https://aclanthology.info/pdf/W/W05/W05-0810.pdf). In Proceedings of the ACL Workshop on Building and Using Parallel Texts (pp. 75-78). Association for Computational Linguistics.

- Lopez, A., & Resnik, P. (2005, June). [Improved HMM alignment models for languages with scarce resources](http://www.aclweb.org/anthology/W05-0812). In Proceedings of the ACL Workshop on Building and Using Parallel Texts (pp. 83-86). Association for Computational Linguistics.

- Martin, J., Mihalcea, R., & Pedersen, T. (2005, June). [Word alignment for languages with scarce resources](http://www.aclweb.org/anthology/W05-0809). In Proceedings of the ACL Workshop on Building and Using Parallel Texts (pp. 65-74). Association for Computational Linguistics.

- Llitjós, A. F., Aranovich, R., & Levin, L. (2005). [Building Machine translation systems for indigenous languages](http://www.cs.cmu.edu/~aria/Papers/FontAranovich_CILLA2_mapuche_quechua(2).pdf). In Second Conference on the Indigenous Languages of Latin America (CILLA II), Texas, USA.

## Automatic Lexical Extraction

**Scientific papers and dictionaries**

- Hunt, B., Chen, E., Schreiner, S. L., & Schwartz, L. (2019). [Community lexical access for an endangered polysynthetic language: An electronic dictionary for St. Lawrence Island Yupik.](https://www.aclweb.org/anthology/N19-4021/) In _NAACL-HLT 2019_, 122.

- Gutierrez-Vasques, X., & Mijangos, V. (2017). [Low-resource bilingual lexicon extraction using graph based word embeddings](https://pdfs.semanticscholar.org/1968/e574af144ca6ecbfe770de031a5f7f96aee6.pdf). _arXiv preprint arXiv:1710.02569_.

- Gutierrez, Ximena. (2015, June). [Bilingual lexicon extraction for a distant language pair using a small parallel corpus](http://www.anthology.aclweb.org/N/N15/N15-2021.pdf). In _NAACL-HLT 2015 Student Research Workshop (SRW)_ (p. 154).

- Lam, K. N., Al Tarouti, F., & Kalita, J. (2014). [Creating lexical resources for endangered languages](http://www.anthology.aclweb.org/W/W14/W14-2207.pdf). ACL 2014, 54. (_Cherokee and Cheyenne_)

## Morphologcal analysis and segmentation

**Software**

- [Inuktitut Morphological Analyzer](http://www.inuktitutcomputing.ca/Uqailaut/index.php)
- [Wixarika Morphological Segmenter](https://github.com/pywirrarika/smtwixes/tree/master/wixnlp)
- [Morphological Analyzer for the Bribri language of the Chibchense family](http://morphology.bribri.net/)
- [Guaraní](https://github.com/apertium/apertium-grn)
- [Cusco Quechua](https://github.com/apertium/apertium-quz)
- [Eastern Apurímac Quechua](https://github.com/apertium/apertium-qve)
- [K'iche'](https://github.com/apertium/apertium-quc)
- [Tseltal](https://github.com/apertium/apertium-tzh)
- [Morfo is an application that analyzes words in several languages (Guarani, K'iche', Qhichwua, etc).](http://plogs.soic.indiana.edu/morfo/)
- [Plains Cree morphological analyzer/generator](https://github.com/UAlbertaALTLab/plains-cree-fsts)

**Scientific Papers**

- Eskander, R., Klavans, J. & Muresan S. (2019) [Unsupervised Morphological Segmentation for Low-Resource Polysynthetic Languages](https://www.aclweb.org/anthology/papers/W/W19/W19-4222/). In Proceedings of the 16th Workshop on Computational Research in Phonetics, Phonology, and Morphology (pp. 189–195).

- Sorokin, A. (2019). [Convolutional neural networks for low-resource morpheme segmentation: baseline or state-of-the-art?](https://www.aclweb.org/anthology/papers/W/W19/W19-4218/) In Proceedings of the 16th Workshop on Computational Research in Phonetics, Phonology, and Morphology (pp. 154–159).

- Micher, J. (2019). [Bootstrapping a Neural Morphological Generator from Morphological Analyzer Output for Inuktitut.](https://scholar.colorado.edu/cgi/viewcontent.cgi?article=1023&context=scil-cmel) In Proceedings of the Workshop on Computational Methods for Endangered Languages (Vol. 2, No. 1, p. 7).

- Escobar Farfan, J. I. (2019). [Nahuatl contemporary writing: studying convergence in the absence of a written norm](http://etheses.whiterose.ac.uk/23958/1/escobar-farfan-phdthesis_032019.pdf) (Doctoral dissertation, University of Sheffield).

- Chen, Emily, and Lane Schwartz. (2018) [A morphological analyzer for St. Lawrence Island/Central Siberian Yupik.](https://www.aclweb.org/anthology/L18-1416) Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC-2018). 2018.

- Cardenas, R. & Zeman, D. (2018) [A Morphological Analyzer for Shipibo-Konibo](https://aclanthology.info/papers/W18-5815/w18-5815). Proceedings of the Fifteenth Workshop on Computational Research in Phonetics, Phonology, and Morphology (pp. 131-139).

- Moeller, S., & Hulden, M. (2018). [Automatic Glossing in a Low-Resource Setting for Language Documentation](http://www.aclweb.org/anthology/W18-4809). In Proceedings of the Workshop on Computational Modeling of Polysynthetic Languages (pp. 84-93).

- Moeller, S., Kazeminejad, G., Cowell, A., & Hulden, M. (2018). [A Neural Morphological Analyzer for Arapaho Verbs Learned from a Finite State Transducer](http://www.aclweb.org/anthology/W18-4802). In Proceedings of the Workshop on Computational Modeling of Polysynthetic Languages (pp. 12-20).

- Littell, P. (2018). [Finite-state morphology for Kwak'wala: A phonological approach](http://www.aclweb.org/anthology/W18-4803). In Proceedings of the Workshop on Computational Modeling of Polysynthetic Languages (pp. 21-30).

- Andriyanets, V., & Tyers, F. (2018). [A prototype finite-state morphological analyser for Chukchi](http://www.aclweb.org/anthology/W18-4804). In Proceedings of the Workshop on Computational Modeling of Polysynthetic Languages (pp. 31-40).

- Kazantseva, A., Maracle, O. B., & Pine, A. (2018). [Kawennón: nis: the Wordmaker for Kanyen'kéha](http://www.aclweb.org/anthology/W18-4806). In Proceedings of the Workshop on Computational Modeling of Polysynthetic Languages (pp. 53-64).

- Kann, K., Mager, M., Meza-Ruiz, I., & Schütze, H. (2018). [Fortification of Neural Morphological Segmentation Models for Polysynthetic Minimal-Resource Languages](https://arxiv.org/pdf/1804.06024.pdf). *16th Annual Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies NAACL-HLT*, New Orleans, Louisiana, US. June, 2018.

- Antti Arppe, Christopher Cox, Mans Hulden, Jordan Lachler, Sjur N. Moshagen, Miikka Silfverberg & Trond Trosterud (2017) [Computational modeling of the verb in Dene languages](http://altlab.artsrn.ualberta.ca/wp-content/uploads/2017/05/ComputationalModelingofVerbsinDeneLanguages_170402.pdf). The case of Tsuut’ina. Working Papers in Athabascan Linguistics (“Red Book” series), Alaska Native Language Center, pp. 51-68.

- Harrigan, A. G., Schmirler, K., Arppe, A., Antonsen, L., Trosterud, T., & Wolvengrey, A. (2017). [Learning from the computational modelling of Plains Cree verbs](https://link.springer.com/article/10.1007/s11525-017-9315-x). Morphology, 27(4), 565-598.

- Cotterell, R., Kirov, C., Sylak-Glassman, J., Walther, G., Vylomova, E., Xia, P., & Faruqui, M. (2017). [CoNLL-SIGMORPHON 2017 Shared Task: Universal Morphological Reinflection in 52 Languages](http://www.aclweb.org/anthology/K17-2001). CoNLL SIGMORPHON, 1. (_Haida, Navajo, Quechua_)

- Bowers, D., Arppe, A., Lachler, J., Moshagen, S., & Trosterud, T. (2017). [A Morphological Parser for Odawa](http://www.aclweb.org/anthology/W/W17/W17-0101.pdf). ComputEL-2, 1.

- Micher, J. C. (2017). [Improving Coverage of an Inuktitut Morphological Analyzer Using a Segmental Recurrent Neural Network](http://www.aclweb.org/anthology/W/W17/W17-0114.pdf). ComputEL-2, 101. (_Inuktitut_)

- Arppe, A., Junker, M. O., & Torkornoo, D. (2017). [Converting a comprehensive lexical database into a computational model: The case of East Cree verb inflection](http://www.aclweb.org/anthology/W/W17/W17-0108.pdf). ComputEL-2, 52. (_Cree_)

- Sylak-Glassman, J., Kirov, C., & Yarowsky, D. (2016). [Remote Elicitation of Inflectional Paradigms to Seed Morphological Analysis in Low-Resource Languages](http://www.lrec-conf.org/proceedings/lrec2016/pdf/1031_Paper.pdf). In LREC. (Also includes some experiments with Nahuatl)

- Christopher Cox, Måns Huldén, Miikka Silfverberg, Jordan Lachler, Sally Rice, Sjur N. Moshagen, Trond Trosterud & Antti Arppe (2016) [Computational modeling of the verb in Dene languages. The case of Tsuut’ina](https://altlab.artsrn.ualberta.ca/wp-content/uploads/2016/07/Tsuutina-FST-DLC-160607B.pdf). Dene Languages Conference, Yellowknife, North-West Territories, Canada, 6-7 June 2016.

- Snoek, C., Thunder, D., Loo, K., Arppe, A., Lachler, J., Moshagen, S., & Trosterud, T. (2014, June). [Modeling the noun morphology of Plains Cree](http://www.anthology.aclweb.org/W/W14/W14-2205.pdf). In Proceedings of the 2014 Workshop on the Use of Computational Methods in the Study of Endangered Languages (pp. 34-42). (_Cree_)

- Gonzales, A. R., & Mamani, R. A. C. (2014). [Morphological Disambiguation and Text Normalization for Southern Quechua Varieties](http://www.aclweb.org/anthology/W14-5305). In Proceedings of the First Workshop on Applying NLP Tools to Similar Languages, Varieties and Dialects (pp. 39-47).

- Dunham, J., Cook, G., & Horner, J. (2014). [LingSync & the Online Linguistic Database: New models for the collection and management of data for language communities, linguists and language learners](http://www.aclweb.org/anthology/W14-2204). In Proceedings of the 2014 Workshop on the Use of Computational Methods in the Study of Endangered Languages (pp. 24-33).

- Assini, A. A. (2013). [Natural language processing and the Mohawk language: creating a finite state morphological parser of Mohawk formal nouns](https://ulir.ul.ie/bitstream/handle/10344/3574/assini_2013_natural.pdf?sequence=5). University of Limerik.

- Vilca, C., David, H., Mariñó, C., Cagniy, F., & Mamani Calderon, E. F. (2013). [Analizador morfológico de la lengua quechua basado en software libre helsinkifinite-statetransducer (hfst)](http://app.tecsup.edu.pe/file/sga/documentos/revistaIi/Ii_1/6.pdf).

- Nicholson, J., Cohn, T., & Baldwin, T. (2012). [Evaluating a Morphological Analyser of Inuktitut](http://www.aclweb.org/anthology/N12-1040). NAACL HLT 2012, 372.

- Martínez-Gil, C., Zempoalteca-Pérez, A., Soancatl-Aguilar, V., de Jesús Estudillo-Ayala, M., Lara-Ramírez, J. E., & Alcántara-Santiago, S. (2012). [Computer Systems for Analysis of Nahuatl](http://www.rcs.cic.ipn.mx/2012_47/Computer%20Systems%20for%20Analysis%20of%20Nahuatl.pdf). Research in Computing Science, 47, 11-16.

- Gasser, M. (2011). [Computational morphology and the teaching of indigenous languages](ftp://ftp.cs.indiana.edu/pub/gasser/stilla.pdf). In Indigenous Languages of Latin America—Actas del Primer Simposio sobre Ensenanza de Lenguas Indıgenas de América Latina (pp. 52-61).

- Porta, A. O. (2010, July). [The use of formal language models in the typology of the morphology of Amerindian languages](http://www.anthology.aclweb.org/P/P10/P10-3019.pdf). In Proceedings of the ACL 2010 Student Research Workshop (pp. 109-113). Association for Computational Linguistics. (_Toba and Quichua_)

- Medina-Urrea, A. (2008). [Affix discovery based on entropy and economy measurements. Computational Linguistics for Less-Studied Languages](http://web.stanford.edu/group/cslipublications/cslipublications/TLS/TLS10-2006/TLS10_Medina-Urrea.pdf). Texas Linguistics Society 10, 99-112.

- Medina-Urrea, A. (2007). [Affix discovery by means of corpora: Experiments for Spanish, Czech, Ralámuli and Chuj](https://link.springer.com/chapter/10.1007/978-3-540-37522-7_13). In Aspects of Automatic Text Analysis (pp. 277-299). Springer, Berlin, Heidelberg.

- Wolfart, H. C., & Pardo, F. (1973). [Computer-assisted linguistic analysis](http://mspace.lib.umanitoba.ca/bitstream/handle/1993/18303/Wolfart,%20Computer-Assisted.pdf?sequence=1), University of Manitoba Anthropology Papers.

## Speech

- Cruz H. and Waring J. (2019). [Deploying Technology to Save Endangered Languages](https://arxiv.org/abs/1908.08971). arXiv preprint arXiv:1908.08971.

- Klavans, J., Morgan, J., LaRocca, S., Micher, J., & Voss, C. (2018). [Challenges in Speech Recognition and Translation of High-Value Low-Density Polysynthetic Languages](http://www.aclweb.org/anthology/W18-1921). In Proceedings of the 13th Conference of the Association for Machine Translation in the Americas (Volume 2: User Papers) (Vol. 2, pp. 283-293).

- Adams, O., Cohn, T., Neubig, G., & Michaud, A. (2017, December). [Phonemic transcription of low-resource tonal languages.](https://www.aclweb.org/anthology/U17-1006) In Proceedings of the Australasian Language Technology Association Workshop 2017 (pp. 53-60).

- Mendels, G., Cooper, E., & Hirschberg, J. (2016). [Babler-data collection from the web to support speech recognition and keyword search](http://www.aclweb.org/anthology/W16-2609). In Proceedings of the 10th Web as Corpus Workshop (pp. 72-81).

- Maldonado, D. M., Villalba Barrientos, R., & Pinto-Roa, D. P. (2016, November). [Eñe’˜ e: Sistema de reconocimiento automático del habla en Guaraní](http://sedici.unlp.edu.ar/bitstream/handle/10915/56979/Documento_completo.pdf?sequence=1). In Simposio Argentino de Inteligencia Artificial (ASAI 2016)-JAIIO 45 (Tres de Febrero, 2016)..

- DiCanio, C., Nam, H., Whalen, D. H., Timothy Bunnell, H., Amith, J. D., & García, R. C. (2013). [Using automatic alignment to analyze endangered language data: Testing the viability of untrained alignment](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5392066/). The Journal of the Acoustical Society of America, 134(3), 2235-2246.(For Mixtec)

- Urrea, A. M., Camacho, J. A. H., & Garcıa, M. A. [Towards the Speech Synthesis of Raramuri: A Unit Selection Approach based on Unsupervised Extraction of Suffix Sequences](https://www.cicling.org/2009/RCS-41/243-256.pdf). Advances in Computational Linguistics, 243.

- Nolazco-Flores, J. A., Salgado-Garza, L. R., & Peña-Díaz, M. (2005, June). [Speaker dependent ASRs for huastec and western-huastec náhuatl languages](https://link.springer.com/chapter/10.1007/11492542_73). In Iberian Conference on Pattern Recognition and Image Analysis (pp. 595-602). Springer, Berlin, Heidelberg.

## POS Tagging

- Jose Pereira-Noriega, Rodolfo Mercado-Gonzales, Andrés Melgar, Marco Sobrevilla-Cabezudo, & Arturo Oncevay-Marcos. (2017). [Ship-LemmaTagger: building an NLP toolkit for a peruvian native language](http://chana.inf.pucp.edu.pe/index.php/en/publications/). In Text, Speech, and Dialogue: 20th International Conference, TSD 2017. Springer.

## Parsing

- Vasquez, A., Aguirre, R. E., Angulo, C., Miller, J., Villanueva, C., Agić, Ž., ... & Oncevay, A. (2018). [Toward Universal Dependencies for Shipibo-Konibo](https://aclanthology.coli.uni-saarland.de/papers/W18-6018/w18-6018). In Proceedings of the Second Workshop on Universal Dependencies (UDW 2018) (pp. 151-161).

- Homola, P. (2011, September). [Parsing a Polysynthetic Language](http://anthology.aclweb.org/R/R11/R11-1079.pdf). In RANLP (pp. 562-567). (_Ayamara_)

- Agić, Ž., Johannsen, A., Plank, B., Martínez, H. A., Schluter, N., & Søgaard, A. (2016). [Multilingual projection for parsing truly low-resource languages.](http://bib.irb.hr/datoteka/827066.agic2016-multilingual.pdf) Transactions of the Association for Computational Linguistics, 4, 301.

## OCR

- Maxwell, M., & Bills, A. (2017). [Endangered Data for Endangered Languages: Digitizing Print dictionaries](http://www.aclweb.org/anthology/W/W17/W17-0112.pdf). ComputEL-2, 85. (_Tzeltal, Muinane, Cubeo_)

- Garrette, D., & Alpert-Abrams, H. (2016). [An Unsupervised Model of Orthographic Variation for Historical Document Transcription](http://www.aclweb.org/anthology/N/N16/N16-1055.pdf). In HLT-NAACL (pp. 467-472).

- Hubert, I., Arppe, A., Lachler, J., & Santos, E. A. (2016). [Training & quality assessment of an optical character recognition model for Northern Haida](https://www.aclweb.org/anthology/L16-1514). In Proceedings of the Tenth International Conference on Language Resources and Evaluation (LREC 2016) (pp. 3227-3234).


## Spell checking

- Carlo Alva and Arturo Oncevay-Marcos. (2017). [Spell-checking based on syllabification and character-level graphs for a peruvian agglutinative language](http://www.aclweb.org/anthology/W17-4116). In Proceedings of the EMNLP 2017 Workshop on Subword & Character Level Models in NLP, SCLeM 2017. ACL Anthology.

-  Schwartz, L., & Chen, E. (2017). [Liinnaqumalghiit: A Web-based Tool for Addressing Orthographic Transparency in St. Lawrence Island/Central Siberian Yupik.](https://core.ac.uk/download/pdf/86663072.pdf) Language documentation and conservation, 11.

## WordNet

- Valencia, D. M., Oncevay-Marcos, A., & Cabezudo, M. A. S. (2018). [WordNet-Shp: Towards the Building of a Lexical Database for a Peruvian Minority Language](http://www.lrec-conf.org/proceedings/lrec2018/pdf/1044.pdf). In LREC.

## Language ID

- Espichán-Linares, A., & Oncevay-Marcos, A. (2017, September). [Language Identification with Scarce Data: A Case Study from Peru](http://chana.inf.pucp.edu.pe/papers/3-language-identification-scarce.pdf). In Annual International Symposium on Information Management and Big Data (pp. 90-105). Springer, Cham.

- Alexandra Espichán-Linares and Arturo Oncevay-Marcos. 2017. [A low-resourced peruvian language identification model](http://ceur-ws.org/Vol-2029/paper3.pdf). In Proceedings of the SIMBig 2017 Track on Applied Natural Language Processing, ANLP 2017. Springer.

- Xia, F., Lewis, C., & Lewis, W. D. (2010). [The Problems of Language Identification within Hugely Multilingual Data Sets](http://mt-archive.info/LREC-2010-Xia.pdf). In LREC.

## Code-Switching and Multilingual NLP

- Mager, M., Çetinoğlu, Ö., & Kann, K. (2019, June). [Subword-Level Language Identification for Intra-Word Code-Switching](https://www.aclweb.org/anthology/papers/N/N19/N19-1201/). In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers) (pp. 2005-2011).

- Dufter, P., Zhao, M., Schmitt, M., Fraser, A., & Schütze, H. (2018). [Embedding Learning Through Multilingual Concept Induction](http://www.aclweb.org/anthology/P18-1141). In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) (Vol. 1, pp. 1520-1530).

- Asgari, E., & Schütze, H. (2017). [Past, Present, Future: A Computational Investigation of the Typology of Tense in 1000 Languages](http://www.aclweb.org/anthology/D17-1011). In Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing (pp. 113-124).

- Garrette, D., Alpert-Abrams, H., Berg-Kirkpatrick, T., & Klein, D. (2015). [Unsupervised Code-Switching for Multilingual Historical Document Transcription](http://www.cs.utexas.edu/~ml/papers/garrette.naacl15.pdf). In HLT-NAACL (pp. 1036-1041).

- King, B., & Abney, S. (2013). [Labeling the languages of words in mixed-language documents using weakly supervised methods](http://www.aclweb.org/anthology/N13-1131). In Proceedings of the 2013 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (pp. 1110-1119). (Also nahutal mixed sentences)

## Tools, documentation and education
**Online available software**
- [Kirrkirr: software for the exploration of indigenous language dictionaries](https://nlp.stanford.edu/kirrkirr/)

**Papers**

- Mercado-Gonzales, R., Pereira-Noriega, J., Cabezudo, M. A. S., & Oncevay-Marcos, A. (2018). [ChAnot: An intelligent annotation tool for indigenous and highly agglutinative languages in Peru.](https://github.com/iapucp/chanot-lrec2018). In LREC.

- Flores Solórzano, S. (2012). [Teclado chibcha: un software lingüístico para los sistemas de escritura de las lenguas bribri y cabécar.](http://repositorio.ucr.ac.cr/bitstream/handle/10669/14459/1110-1580-1-SM.pdf) Revista de Filología y Lingüística de la Universidad de Costa Rica Vol. 36 Núm. 2.

- Kuhn, J. (2004). [Applying computational linguistic techniques in a documentary project for Q’anjob’al (Mayan, Guatemala)](http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=38AE54494D1E31D064F78F599CF0AEE0?doi=10.1.1.154.6408&rep=rep1&type=pdf). In In Proceedings of LREC 2004.

- Lessard, G., Brinklow, N., & Levison, M. (2018). [Natural Language Generation for Polysynthetic Languages: Language Teaching and Learning Software for Kanyen’kéha (Mohawk)](http://www.aclweb.org/anthology/W18-4805). In Proceedings of the Workshop on Computational Modeling of Polysynthetic Languages (pp. 41-52).

- Manning, C. D., Jansz, K., & Indurkhya, N. (2001). [Kirrkirr: Software for browsing and visual exploration of a structured Warlpiri dictionary](https://nlp.stanford.edu/kirrkirr/doc/ach-allc2000-ver5-single.pdf). Literary and Linguistic Computing, 16(2), 135-151.

- Jansz, K., Manning, C., & Indurkhya, N. (1999). [Kirrkirr: Interactive visualisation and multimedia from a structured Warlpiri dictionary](https://nlp.stanford.edu/kirrkirr/ausweb99/paper.html). Proceedings of AusWeb99, the Fifth Australian World Wide Web Conference, pp. 302-316.

## Computational Linguistic Analyze and Surveys

Vera J. and Palma W. (2020) [Laplacian spectrum approach to linguistic complexity: a casestudy on indigenous languages of the America](https://www.researchgate.net/publication/340003576_Laplacian_spectrum_approach_to_linguistic_complexity_a_case_study_on_indigenous_languages_of_the_Americas). EPL (Europhysics Letters).

- van Esch, D., Foley, B., & San, N. (2019). [Future Directions in Technological Support for Language Documentation](https://scholar.colorado.edu/cgi/viewcontent.cgi?article=1007&context=scil-cmel). In Proceedings of the Workshop on Computational Methods for Endangered Languages (Vol. 1, No. 1, p. 3).

- Maheshwari, A., Bouscarrat, L., & Cook, P. (2018, May). [Towards Language Technology for Mi’kmaq](https://www.aclweb.org/anthology/L18-1653/). In Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC-2018).

- Camacho, L., & Zevallos, R. (2018)[Siminchikkunarayku](https://www.researchgate.net/profile/Luis_Camacho15/publication/329718519_Siminchikkunarayku_Linguistica_computacional_para_la_revitalizacion_y_el_poliglotismo_Hoja_de_Ruta/links/5c18103ca6fdcc494ffc5ffa/Siminchikkunarayku-Lingueistica-computacional-para-la-revitalizacion-y-el-poliglotismo-Hoja-de-Ruta.pdf). Fundación Siminchikkunarayku, Pontificia Universidad Católica del Perú. 

- Mager, M., Gutierrez-Vasques, X., Sierra, G., & Meza, I. (2018). [Challenges of language technologies for the indigenous languages of the Americas](https://aclanthology.coli.uni-saarland.de/papers/C18-1006/c18-1006). In Proceedings of the 27th International Conference on Computational Linguistics (pp. 55–69).

- Littell, P., Kazantseva, A., Kuhn, R., Pine, A., Arppe, A., Cox, C., & Junker, M. O. (2018). [Indigenous language technologies in Canada: Assessment, challenges, and successes](http://www.aclweb.org/anthology/C18-1222). In Proceedings of the 27th International Conference on Computational Linguistics (pp. 2620-2632).

- Gutierrez-Vasques, X., & Mijangos, V. (2018). [Comparing morphological complexity of Spanish, Otomi and Nahuatl](http://aclweb.org/anthology/W18-4604). In Proceedings of the Workshop on Linguistic Complexity and Natural Language Processing (pp. 30-37).

- Klavans, J. L. (2018). [Computational Challenges for Polysynthetic Languages](http://www.aclweb.org/anthology/W18-4801). In Proceedings of the Workshop on Computational Modeling of Polysynthetic Languages (pp. 1-11).

## Contact

This effort can be completed only with the cooperation of all visitors. If you know about some work in this field, please let me know and push to this repositoy or send an email to mmager [at] turing.iimas.unam.mx or visit my personal [web page](http://code.kiutz.com).

## How to cite

If you found this information usefull for your academic research please acknowledge its use with a citation:

Mager, M., Gutierrez. X., Sierra, G., and Meza, I. (2018, August).  *Challenges of language technologies for the Americas indigenous languages*. In Proceedings of the 27th international conference on Computational linguistics. Association for Computational Linguistics.

```bibtex
@InProceedings{C18-1006,
  author = 	"Mager, Manuel
		and Gutierrez-Vasques, Ximena
		and Sierra, Gerardo
		and Meza-Ruiz, Ivan",
  title = 	"Challenges of language technologies for the indigenous languages of the Americas",
  booktitle = 	"Proceedings of the 27th International Conference on Computational Linguistics",
  year = 	"2018",
  publisher = 	"Association for Computational Linguistics",
  pages = 	"55--69",
  location = 	"Santa Fe, New Mexico, USA",
  url = 	"http://aclweb.org/anthology/C18-1006"
}
```

## Links

- [**Awesome Natives in Tech** List of researchers and natives active in technology](https://github.com/nativesintech)
- [**Endangered Languages (Github List)**](https://github.com/LowResourceLanguages/endangered-languages)

