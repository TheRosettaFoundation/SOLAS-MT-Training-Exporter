# SOLAS-MT-Training-Exporter
Subject Matter specialized Machine Translation (MT) engines need for their training specifically targeted bilingual corpora. SOLAS MT Training Exporter makes use of XLIFF corpora stored after roundtrip completion that are ideal metadata rich content for profiling the desired corpora.  This invention builds on the fact that XLIFF corpora created as a side effect of localising in an open ITS 2.0 aware XLIFF based service architecture are: 1) Aligned bilingual corpora 2) Metadata rich. The invention uses a subset of metadata that can be used for MT training corpora profiling. Such service is ideally built upon a XML database data store underlying the open localisation service architecture.
 
SOLAS MT Training Exporter supports open standards; it is ITS 2 aware by design via the XLIFF 1.2. and XLIFF 2.0 Mapping. It is a reference implementation of the XLIFF 2.0 and ITS 2.0 standards. This component serves as a RESTful wrapper upon an XML database datastore. It allows for XML native queries over the aligned bilingual corpora that have been created as a side effect of running localisation within an open service oriented architecture based on the standardized XML exchange format (XLIFF).

**Coded by:**
* [Phillip O’Duffy](https://github.com/PhilipUL)
* [David O' Carroll](https://github.com/spaceindaver)
* [Ray Kearney](https://github.com/raythered)

## License notice
This software is licensed under the terms of the GNU LESSER GENERAL PUBLIC LICENSE Version 3, 29 June 2007 For full terms see License.txt or http://www.gnu.org/licenses/lgpl-3.0.txt

## Live demo 
* http://demo.solas.uni.me/corpus-ui/

## References
 * http://www.w3.org/International/multilingualweb/lt/wiki/images/2/22/D3.1.2.pdf
 * http://www.w3.org/International/multilingualweb/rome/posters/mlwlt_rome2013poster-07.pdf

## Acknowledgement
This research is supported by "FP7-ICT-2011-7 - Language technologies" Project "MultilingualWeb-LT (LT-Web) - Language Technology in the Web" (287815 - CSA).
