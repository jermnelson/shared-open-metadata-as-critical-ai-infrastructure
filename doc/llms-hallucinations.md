<h2><i class="bi-chat-square-dots"></i> Hallucinations of Large Language Models</h2>

A persistent problem, even for the frontier Large Language Models from OpenAI, Antropic, Google, and
Deep Seek, is the tendency for these models to fabricate facts in an increasingly pervasive fashion.
Large Language Models are transformer-based neural networks that predict
the next series of tokens based on context. This variability means that the "next token" is a
probabilistic rather than deterministic, so that over millions of predictions, incorrect or improbable 
outputs are intrinsic to this technology. 

In a recent paper[^1], Open AI researchers assert that hallucinations
are a consequence of the how models are trained and awarded for guessing on benchmarks and tests,
and not necessarily because of the nature of the LLM architecture itself. Interestingly,
Antropic researchers note that their LLMs actually tend to not speculate but will
do so as a result of competing features in the model that are activated depending on the
prompt. This report also links how LLMs hallucinations are related to jail breaking
LLMs as prompts shift the model to use different circuits to produce the model's outputs.[^2]
 
Concerning for metadata workflows, LLM hallucinations could result in fabricated or incorrect
subject assertions or invented identifiers like ISBNs or DOIs.

### Reducing Hallucinations
As LLMs have improved, their output has improved as the following example illustrates.

From an ai4lam Metadata Working Group meeting on 12 November 2024[^3], ChatGPT 4o model
generated a MARC record based on this prompt for a fictitious book:

**Prompt**: Create a MARC 21 record for book Two hundred años de soledad

**Model Response**:

Certainly! The MARC 21 format is a standard for the representation and communication of bibliographic and related information in machine-readable form. Below is a MARC 21 record example for a fictional book titled "Two Hundred Años de Soledad" (a play on Gabriel García Márquez's "One Hundred Years of Solitude", assuming it's a similar work in terms of bibliographic elements).

```plaintext
=Leader  00000nam a2200000 i 4500
=001     123456789
=005     20231012120000.0
=008     231012s2023    xxu           000 1 spa d
=020    \\$a9781234567890
=040    \\$aXYZ$cXYZ$eIFN
=041  1 \$aspa$heng
=100  1\$aDoe, Juan.
=245  10$aTwo hundred años de soledad /$cJuan Doe.
=246  3\$a200 años de soledad
=250    \$aPrimera edición.
=260    \$aCiudad Inexistente :$bEditorial Fantasía,$c2023.
=300    \$a350 páginas ;$c23 cm.
=336    \$atexto$btxt$2rdacontent
=337    \$asin mediado$bn$2rdamedia
=338    \$avolumen$bnc$2rdacarrier
=500    \\$aObra de ficción.
=504    \\$aIncluye referencias bibliográficas.
=520    \\$aEsta novela narra la historia de la familia ficticia y sus encuentros mágicos en el pueblo de Macondo a lo largo de doscientos años.
=650  \0$aFicción mágica.
=650  \0$aLiteratura hispanoamericana.
=700  1\$aPérez, María,$etraductor.
=852  \\$aBiblioteca de Ejemplo
```

### Using the same prompt now with GPT-5:

I can draft a MARC 21 bibliographic record, but I’ll need details like author, publisher, place, date, pages, ISBN, and language to finalize it. Here’s a provisional RDA-compliant record you can fill in:

```plaintext
LDR 00000nam a2200000 i 4500
001 tmp-20251016-0001
003 [your agency code]
005 20251016T000000.0
008 [YYYYMMDD] s[YYYY]    xx                000 0 und
040 ## a[youragencycode]b eng erdac [your agency code]
245 00 a Two hundred años de soledad.
246 3# a 200 años de soledad
264 #1 a[Placeofpublicationnotidentified]:b [publisher not identified], c [date of publication not identified].
300 ## a [extent, e.g., 352 pages] ; c [height, e.g., 23 cm]
336 ## a text b txt \2 rdacontent
337 ## aunmediatedb n $2 rdamedia
338 ## avolumeb nc $2 rdacarrier
500 ## a Title appears in mixed English and Spanish.
546 ## a Language of text not identified.
588 ## $a Description based on title page.
```
Optional fields you can add when known:

```plaintext
020 ## a [ISBN]
041 ## a [language code(s), e.g., spa or eng]
100 1# a[Author’sname].24510a Two hundred años de soledad / c [author’s name].
250 ## a [Edition statement].
264 #4 c [copyright year].
504 ## a Includes bibliographical references.
650 #0 a[Subjectheading]v [Form subdivision if applicable].
655 #7 a [Form/genre term, e.g., Novels] \2 lcgft
700 1# a[Contributorname]e [role, e.g., translator].
```

Provide the missing details (author, publisher, place, year, pages, ISBN, language), and I’ll finalize the record with accurate fixed fields (008) and indicators.

[^1]: [Why Language Models Hallucinate](https://openai.com/index/why-language-models-hallucinate/)
[^2]: [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model)
[^3]: [11/12/2024 Jupyter Notebook](https://github.com/AI4LAM/metadata-working-group/blob/main/notebooks/2024-11-12.ipynb)
