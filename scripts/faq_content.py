"""Patient FAQ, reviewed for source support 2026-09-13; physician review not asserted."""
from html import escape as e
PMR='https://www.aapmr.org/about-physiatry/about-physical-medicine-rehabilitation'
EMG='https://www.mayoclinic.org/tests-procedures/emg/about/pac-20393913'
FAQ=[
 ('physiatre','Qu’est-ce qu’un physiatre?','What is a physiatrist?',
 'Un physiatre est un médecin spécialiste en médecine physique et réadaptation. Il évalue les problèmes qui touchent les muscles, les articulations et le système nerveux, avec pour objectifs la fonction, l’autonomie et la qualité de vie.',
 'A physiatrist is a physician specializing in physical medicine and rehabilitation. They assess muscle, joint and nervous system conditions, focusing on function, independence and quality of life.',PMR,'AAPM&R'),
 ('motifs','Pour quels problèmes consulter en physiatrie?','When should I see a physiatrist?',
 'Une consultation peut être utile pour des douleurs musculosquelettiques, certaines atteintes nerveuses ou des difficultés fonctionnelles après une maladie neurologique. Votre médecin peut vous orienter selon votre situation.',
 'A consultation may help with musculoskeletal pain, certain nerve conditions or functional difficulties following neurological illness. Your physician can advise whether physiatry is appropriate for you.',PMR,'AAPM&R'),
 ('montreal','Où consulter le Dr Andrei Bursuc à Montréal?','Where does Dr Andrei Bursuc see patients in Montréal?',
 'Le Dr Bursuc consulte à la {name}, au {street}, {city}. Pour un rendez-vous, appelez le {phone}.',
 'Dr Bursuc sees patients at {name}, {street}, {city}. To arrange an appointment, call {phone}.',None,None),
 ('reference','Faut-il une référence médicale pour consulter?','Do I need a physician referral?',
 'Une référence médicale est requise. Contactez la clinique au {phone} pour connaître la procédure et les documents à transmettre, notamment pour une demande d’EMG.',
 'A physician referral is required. Contact the clinic at {phone} for the booking process and required documents, including an EMG request when applicable.',None,None),
 ('services','Quels services le Dr Bursuc offre-t-il?','Which services does Dr Bursuc offer?',
 'Sa pratique comprend l’électromyographie, la gestion de la spasticité, les infiltrations échoguidées et les injections de toxine botulinique pour la migraine chronique. L’évaluation médicale détermine les options adaptées à votre situation.',
 'His practice includes electromyography, spasticity management, ultrasound-guided injections and botulinum toxin injections for chronic migraine. Medical assessment determines which options are appropriate for you.',None,None),
 ('emg','À quoi sert un examen d’électromyographie (EMG)?','What is an electromyography (EMG) test for?',
 'L’EMG et les études de conduction nerveuse évaluent les muscles et les nerfs. Ils peuvent aider à rechercher la cause d’engourdissements ou d’une faiblesse, notamment une compression nerveuse.',
 'EMG and nerve conduction studies assess muscles and nerves. They can help investigate numbness or weakness, including nerve compression.',EMG,'Mayo Clinic'),
 ('preparation-emg','Comment se préparer à un EMG?','How should I prepare for an EMG?',
 'Évitez les crèmes sur la peau avant l’examen. Signalez vos médicaments, notamment les anticoagulants, ainsi que tout stimulateur cardiaque ou trouble de coagulation. Ne modifiez pas un traitement sans consigne médicale.',
 'Avoid skin creams before the test. Report medications, particularly blood thinners, and any pacemaker or bleeding disorder. Do not change treatment without medical instructions.',EMG,'Mayo Clinic'),
 ('douleur-emg','Est-ce qu’un EMG est douloureux?','Is an EMG painful?',
 'Les stimulations électriques et l’aiguille peuvent être inconfortables. Signalez toute douleur à la personne qui réalise l’examen.',
 'Electrical stimulation and the needle can be uncomfortable. Tell the examiner if you experience pain.',EMG,'Mayo Clinic'),
 ('frais','Comment connaître les délais et les frais éventuels?','How can I check wait times and possible fees?',
 'Contactez directement la clinique au {phone}. Elle pourra préciser les délais, les modalités de couverture et les frais éventuels selon le service demandé.',
 'Contact the clinic at {phone}. Staff can clarify wait times, coverage arrangements and any fees for the requested service.',None,None),
 ('outils','Les outils d’éducation médicale sont-ils accessibles au public?','Are the medical education tools publicly accessible?',
 'Oui. La section Éducation médicale propose des explorateurs des nerfs, des fascicules intraneuraux, des blocs moteurs et des muscles en échographie. Ils sont destinés à l’apprentissage et ne remplacent pas une évaluation médicale.',
 'Yes. The Medical education section offers nerve, intraneural fascicle, motor block and muscle ultrasound explorers. They support learning and do not replace a medical assessment.',None,None)
]
def cards(lang,clinic,items):
 fr=lang=='fr';out=''
 for key,qf,qe,af,ae,url,label in items:
  answer=(af if fr else ae).format(**clinic)
  source=f'<small class="faq-source">Source : <a href="{url}">{label}</a></small>' if url else ''
  out+=f'<details id="{key}"><summary>{e(qf if fr else qe)}</summary><div class="faq-answer"><p>{e(answer)}</p>{source}</div></details>'
 return out

def faq_html(lang,clinic,home):
 fr=lang=='fr'
 title='Questions fréquentes.' if fr else 'Frequently asked questions.'
 intro='Consultation en physiatrie à Montréal, EMG et rendez-vous : les réponses aux questions des patients.' if fr else 'Physiatry in Montréal, EMG and appointments: answers to common patient questions.'
 note='Informations générales. Les recommandations pour votre situation sont précisées lors de la consultation.' if fr else 'General information. Recommendations for your situation are discussed during your consultation.'
 return f'<main id="main"><section class="edu-hero"><div class="wrap"><p class="eyebrow">Dr Andrei Bursuc · Montréal</p><h1>{title}</h1><p>{intro}</p></div></section><section class="section wrap"><div class="faq-list">{cards(lang,clinic,FAQ)}</div><p class="faq-footer">{note}</p><div class="actions"><a class="button" href="tel:{clinic["phoneLink"]}">{"Appeler la clinique" if fr else "Call the clinic"} · {e(clinic["phone"])}</a><a class="button secondary" href="{home}#consultations">{"Coordonnées" if fr else "Contact details"}</a></div></section></main>'

def faq_teaser(lang,url):
 fr=lang=='fr'
 # Questions link to real HTML answers, so they work without client scripts.
 links=''.join(f'<a class="faq-question-link" href="{url}#{key}">{e(qf if fr else qe)} <span aria-hidden="true">↗</span></a>' for key,qf,qe,*rest in [FAQ[0],FAQ[3],FAQ[5]])
 return f'<section class="section soft"><div class="wrap"><div class="section-head"><div><p class="eyebrow">{"Pour les patients" if fr else "For patients"}</p><h2>{"Vos questions, nos réponses." if fr else "Your questions, answered."}</h2></div><a class="button secondary" href="{url}">{"Toutes les questions" if fr else "All questions"}</a></div><div class="faq-question-links">{links}</div></div></section>'
