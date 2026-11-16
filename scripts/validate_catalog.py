"""Validate public OYYO catalog identities, requirements, cards and relative links."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parent.parent
catalog=json.loads((ROOT/'catalog/models.json').read_text(encoding='utf-8'))
models=catalog['models'];assert len(models)==15
assert len({m['id'] for m in models})==len(models)
assert len({m['displayName'] for m in models})==len(models)
for m in models:
 assert m['displayName'].startswith('OYYO ')
 assert m['execution']=='local' and m['availability']=='runtime-download-candidate'
 assert m['sizeBytes']>0 and 0<m['minRamGB']<=m['recommendedRamGB']
 assert m['hardwareRequirementsAreEstimates'] is True
 assert re.fullmatch('[a-f0-9]{64}',m['sha256'])
 assert m['exampleRequest'] and m['specialization'] and m['limitations']
 assert not any(k in m for k in ['sourceUrl','upstream','qualificationScore','passed'])
 card=ROOT/m['modelCard'];assert card.is_file()
 text=card.read_text(encoding='utf-8')
 for value in [m['displayName'],m['id'],m['sha256'],m['exampleRequest']]:assert value in text,(card,value)
options=json.loads((ROOT/'catalog/additional-options.json').read_text(encoding='utf-8'))['options']
assert len(options)==3
options_by_id={option['id']:option for option in options}
assert options_by_id['OYYO-NotzUP-Tiny-ALL']['tiersUseSameWeights'] is True
signals=options_by_id['OYYO-SIGNAL-TINY-ALL']
assert signals['release']=='2026.11.1' and signals['applicationBaseline']=='Android 0.8.0'
assert signals['offlineInference'] is True and signals['externalModelApi'] is False
assert signals['requiresUserConfirmation'] is True and signals['realOrderSubmission'] is False
assert [variant['tier'] for variant in signals['variants']]==['S1','S2','S3','S4']
for variant in signals['variants']:
 assert variant['sizeBytes']>0 and re.fullmatch('[a-f0-9]{64}',variant['sha256'])
assert options_by_id['oyyo-prime-s3-0.13']['execution']=='connected-account'
assert options_by_id['oyyo-prime-s3-0.13']['offline'] is False
for option in options:assert (ROOT/option['modelCard']).is_file()
signals_card=(ROOT/signals['modelCard']).read_text(encoding='utf-8')
for value in [signals['id'],signals['release'],signals['applicationBaseline']]:
 assert value in signals_card,(signals['modelCard'],value)
links=0
for f in ROOT.rglob('*.md'):
 if '.git' in f.parts:continue
 for target in re.findall(r'\]\(([^)]+)\)',f.read_text(encoding='utf-8-sig')):
  if re.match(r'^[a-z]+:',target) or target.startswith('#'):continue
  target=target.split('#')[0]
  if not target:continue
  assert (f.parent/target).exists(),(f,target)
  links+=1
print(json.dumps({'localCandidates':len(models),'additionalOptions':len(options),'relativeLinksVerified':links,'valid':True}))
