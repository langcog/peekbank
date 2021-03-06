# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-08 21:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.IntegerField(default=None, primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.datetime.now, max_length=255)),
                ('version', models.CharField(default=None, max_length=255)),
            ],
            options={
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='Administration',
            fields=[
                ('administration_id', models.IntegerField(primary_key=True, serialize=False)),
                ('age', models.FloatField(default=None, null=True)),
                ('lab_age', models.FloatField(default=None, null=True)),
                ('lab_age_units', models.CharField(choices=[['days', 'days'], ['months', 'months'], ['years', 'years'], ['epochs', 'epochs']], default=None, max_length=63, null=True)),
                ('monitor_size_x', models.IntegerField(default=None, null=True)),
                ('monitor_size_y', models.IntegerField(default=None, null=True)),
                ('sample_rate', models.FloatField(default=None, null=True)),
                ('tracker', models.CharField(default=None, max_length=255, null=True)),
                ('coding_method', models.CharField(choices=[['eyetracking', 'eyetracking'], ['manual gaze coding', 'manual gaze coding'], ['automated gaze coding', 'automated gaze coding']], default=None, max_length=255, null=True)),
            ],
            options={
                'db_table': 'administrations',
            },
        ),
        migrations.CreateModel(
            name='AOI_Region_Set',
            fields=[
                ('aoi_region_set_id', models.IntegerField(primary_key=True, serialize=False)),
                ('l_x_max', models.IntegerField(default=None, null=True)),
                ('l_x_min', models.IntegerField(default=None, null=True)),
                ('l_y_max', models.IntegerField(default=None, null=True)),
                ('l_y_min', models.IntegerField(default=None, null=True)),
                ('r_x_max', models.IntegerField(default=None, null=True)),
                ('r_x_min', models.IntegerField(default=None, null=True)),
                ('r_y_max', models.IntegerField(default=None, null=True)),
                ('r_y_min', models.IntegerField(default=None, null=True)),
            ],
            options={
                'db_table': 'aoi_region_sets',
            },
        ),
        migrations.CreateModel(
            name='AOI_Timepoint',
            fields=[
                ('aoi_timepoint_id', models.IntegerField(primary_key=True, serialize=False)),
                ('aoi', models.CharField(choices=[['target', 'target'], ['distractor', 'distractor'], ['other', 'other'], ['missing', 'missing']], max_length=255)),
                ('t_norm', models.IntegerField()),
                ('administration_id', models.ForeignKey(db_column='administration_id', on_delete=django.db.models.deletion.CASCADE, to='db.Administration')),
            ],
            options={
                'db_table': 'aoi_timepoints',
            },
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('dataset_id', models.IntegerField(primary_key=True, serialize=False)),
                ('lab_dataset_id', models.CharField(default=None, max_length=255, null=True)),
                ('dataset_name', models.CharField(max_length=255, unique=True)),
                ('shortcite', models.CharField(default=None, max_length=255, null=True)),
                ('cite', models.CharField(default=None, max_length=1023, null=True)),
            ],
            options={
                'db_table': 'datasets',
            },
        ),
        migrations.CreateModel(
            name='Stimulus',
            fields=[
                ('stimulus_id', models.IntegerField(primary_key=True, serialize=False)),
                ('stimulus_novelty', models.CharField(choices=[['novel', 'novel'], ['familiar', 'familiar']], default=None, max_length=255, null=True)),
                ('original_stimulus_label', models.CharField(default=None, max_length=255, null=True)),
                ('english_stimulus_label', models.CharField(default=None, max_length=255, null=True)),
                ('stimulus_image_path', models.CharField(default=None, max_length=1023, null=True)),
                ('lab_stimulus_id', models.CharField(default=None, max_length=255, null=True)),
                ('dataset_id', models.ForeignKey(db_column='dataset_id', on_delete=django.db.models.deletion.CASCADE, to='db.Dataset')),
            ],
            options={
                'db_table': 'stimuli',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.IntegerField(primary_key=True, serialize=False)),
                ('sex', models.CharField(choices=[['female', 'female'], ['male', 'male'], ['other', 'other'], ['unspecified', 'unspecified']], default=None, max_length=255, null=True)),
                ('native_language', models.CharField(default=None, max_length=255, null=True)),
                ('lab_subject_id', models.CharField(default=None, max_length=255, null=True)),
            ],
            options={
                'db_table': 'subjects',
            },
        ),
        migrations.CreateModel(
            name='Trial',
            fields=[
                ('trial_id', models.IntegerField(primary_key=True, serialize=False)),
                ('trial_order', models.IntegerField(default=None, null=True)),
            ],
            options={
                'db_table': 'trials',
            },
        ),
        migrations.CreateModel(
            name='Trial_Type',
            fields=[
                ('trial_type_id', models.IntegerField(primary_key=True, serialize=False)),
                ('full_phrase', models.CharField(max_length=1023, null=True)),
                ('full_phrase_language', models.CharField(choices=[['aar', 'aar'], ['abk', 'abk'], ['ace', 'ace'], ['ach', 'ach'], ['ada', 'ada'], ['ady', 'ady'], ['afa', 'afa'], ['afh', 'afh'], ['afr', 'afr'], ['ain', 'ain'], ['aka', 'aka'], ['akk', 'akk'], ['alb', 'alb'], ['ale', 'ale'], ['alg', 'alg'], ['alt', 'alt'], ['amh', 'amh'], ['ang', 'ang'], ['anp', 'anp'], ['apa', 'apa'], ['ara', 'ara'], ['arc', 'arc'], ['arg', 'arg'], ['arm', 'arm'], ['arn', 'arn'], ['arp', 'arp'], ['art', 'art'], ['arw', 'arw'], ['asm', 'asm'], ['ast', 'ast'], ['ath', 'ath'], ['aus', 'aus'], ['ava', 'ava'], ['ave', 'ave'], ['awa', 'awa'], ['aym', 'aym'], ['aze', 'aze'], ['bad', 'bad'], ['bai', 'bai'], ['bak', 'bak'], ['bal', 'bal'], ['bam', 'bam'], ['ban', 'ban'], ['baq', 'baq'], ['bas', 'bas'], ['bat', 'bat'], ['bej', 'bej'], ['bel', 'bel'], ['bem', 'bem'], ['ben', 'ben'], ['ber', 'ber'], ['bho', 'bho'], ['bih', 'bih'], ['bik', 'bik'], ['bin', 'bin'], ['bis', 'bis'], ['bla', 'bla'], ['bnt', 'bnt'], ['tib', 'tib'], ['bos', 'bos'], ['bra', 'bra'], ['bre', 'bre'], ['btk', 'btk'], ['bua', 'bua'], ['bug', 'bug'], ['bul', 'bul'], ['bur', 'bur'], ['byn', 'byn'], ['cad', 'cad'], ['cai', 'cai'], ['car', 'car'], ['cat', 'cat'], ['cau', 'cau'], ['ceb', 'ceb'], ['cel', 'cel'], ['cze', 'cze'], ['cha', 'cha'], ['chb', 'chb'], ['che', 'che'], ['chg', 'chg'], ['chi', 'chi'], ['chk', 'chk'], ['chm', 'chm'], ['chn', 'chn'], ['cho', 'cho'], ['chp', 'chp'], ['chr', 'chr'], ['chu', 'chu'], ['chv', 'chv'], ['chy', 'chy'], ['cmc', 'cmc'], ['cop', 'cop'], ['cor', 'cor'], ['cos', 'cos'], ['cpe', 'cpe'], ['cpf', 'cpf'], ['cpp', 'cpp'], ['cre', 'cre'], ['crh', 'crh'], ['crp', 'crp'], ['csb', 'csb'], ['cus', 'cus'], ['wel', 'wel'], ['dak', 'dak'], ['dan', 'dan'], ['dar', 'dar'], ['day', 'day'], ['del', 'del'], ['den', 'den'], ['ger', 'ger'], ['dgr', 'dgr'], ['din', 'din'], ['div', 'div'], ['doi', 'doi'], ['dra', 'dra'], ['dsb', 'dsb'], ['dua', 'dua'], ['dum', 'dum'], ['dut', 'dut'], ['dyu', 'dyu'], ['dzo', 'dzo'], ['efi', 'efi'], ['egy', 'egy'], ['eka', 'eka'], ['gre', 'gre'], ['elx', 'elx'], ['eng', 'eng'], ['enm', 'enm'], ['epo', 'epo'], ['est', 'est'], ['ewe', 'ewe'], ['ewo', 'ewo'], ['fan', 'fan'], ['fao', 'fao'], ['per', 'per'], ['fat', 'fat'], ['fij', 'fij'], ['fil', 'fil'], ['fin', 'fin'], ['fiu', 'fiu'], ['fon', 'fon'], ['fre', 'fre'], ['frm', 'frm'], ['fro', 'fro'], ['frr', 'frr'], ['frs', 'frs'], ['fry', 'fry'], ['ful', 'ful'], ['fur', 'fur'], ['gaa', 'gaa'], ['gay', 'gay'], ['gba', 'gba'], ['gem', 'gem'], ['geo', 'geo'], ['gez', 'gez'], ['gil', 'gil'], ['gla', 'gla'], ['gle', 'gle'], ['glg', 'glg'], ['glv', 'glv'], ['gmh', 'gmh'], ['goh', 'goh'], ['gon', 'gon'], ['gor', 'gor'], ['got', 'got'], ['grb', 'grb'], ['grc', 'grc'], ['grn', 'grn'], ['gsw', 'gsw'], ['guj', 'guj'], ['gwi', 'gwi'], ['hai', 'hai'], ['hat', 'hat'], ['hau', 'hau'], ['haw', 'haw'], ['heb', 'heb'], ['her', 'her'], ['hil', 'hil'], ['him', 'him'], ['hin', 'hin'], ['hit', 'hit'], ['hmn', 'hmn'], ['hmo', 'hmo'], ['hrv', 'hrv'], ['hsb', 'hsb'], ['hun', 'hun'], ['hup', 'hup'], ['iba', 'iba'], ['ibo', 'ibo'], ['ice', 'ice'], ['ido', 'ido'], ['iii', 'iii'], ['ijo', 'ijo'], ['iku', 'iku'], ['ile', 'ile'], ['ilo', 'ilo'], ['ina', 'ina'], ['inc', 'inc'], ['ind', 'ind'], ['ine', 'ine'], ['inh', 'inh'], ['ipk', 'ipk'], ['ira', 'ira'], ['iro', 'iro'], ['ita', 'ita'], ['jav', 'jav'], ['jbo', 'jbo'], ['jpn', 'jpn'], ['jpr', 'jpr'], ['jrb', 'jrb'], ['kaa', 'kaa'], ['kab', 'kab'], ['kac', 'kac'], ['kal', 'kal'], ['kam', 'kam'], ['kan', 'kan'], ['kar', 'kar'], ['kas', 'kas'], ['kau', 'kau'], ['kaw', 'kaw'], ['kaz', 'kaz'], ['kbd', 'kbd'], ['kha', 'kha'], ['khi', 'khi'], ['khm', 'khm'], ['kho', 'kho'], ['kik', 'kik'], ['kin', 'kin'], ['kir', 'kir'], ['kmb', 'kmb'], ['kok', 'kok'], ['kom', 'kom'], ['kon', 'kon'], ['kor', 'kor'], ['kos', 'kos'], ['kpe', 'kpe'], ['krc', 'krc'], ['krl', 'krl'], ['kro', 'kro'], ['kru', 'kru'], ['kua', 'kua'], ['kum', 'kum'], ['kur', 'kur'], ['kut', 'kut'], ['lad', 'lad'], ['lah', 'lah'], ['lam', 'lam'], ['lao', 'lao'], ['lat', 'lat'], ['lav', 'lav'], ['lez', 'lez'], ['lim', 'lim'], ['lin', 'lin'], ['lit', 'lit'], ['lol', 'lol'], ['loz', 'loz'], ['ltz', 'ltz'], ['lua', 'lua'], ['lub', 'lub'], ['lug', 'lug'], ['lui', 'lui'], ['lun', 'lun'], ['luo', 'luo'], ['lus', 'lus'], ['mac', 'mac'], ['mad', 'mad'], ['mag', 'mag'], ['mah', 'mah'], ['mai', 'mai'], ['mak', 'mak'], ['mal', 'mal'], ['man', 'man'], ['mao', 'mao'], ['map', 'map'], ['mar', 'mar'], ['mas', 'mas'], ['may', 'may'], ['mdf', 'mdf'], ['mdr', 'mdr'], ['men', 'men'], ['mga', 'mga'], ['mic', 'mic'], ['min', 'min'], ['mis', 'mis'], ['mkh', 'mkh'], ['mlg', 'mlg'], ['mlt', 'mlt'], ['mnc', 'mnc'], ['mni', 'mni'], ['mno', 'mno'], ['moh', 'moh'], ['mon', 'mon'], ['mos', 'mos'], ['mul', 'mul'], ['mun', 'mun'], ['mus', 'mus'], ['mwl', 'mwl'], ['mwr', 'mwr'], ['myn', 'myn'], ['myv', 'myv'], ['nah', 'nah'], ['nai', 'nai'], ['nap', 'nap'], ['nau', 'nau'], ['nav', 'nav'], ['nbl', 'nbl'], ['nde', 'nde'], ['ndo', 'ndo'], ['nds', 'nds'], ['nep', 'nep'], ['new', 'new'], ['nia', 'nia'], ['nic', 'nic'], ['niu', 'niu'], ['nno', 'nno'], ['nob', 'nob'], ['nog', 'nog'], ['non', 'non'], ['nor', 'nor'], ['nqo', 'nqo'], ['nso', 'nso'], ['nub', 'nub'], ['nwc', 'nwc'], ['nya', 'nya'], ['nym', 'nym'], ['nyn', 'nyn'], ['nyo', 'nyo'], ['nzi', 'nzi'], ['oci', 'oci'], ['oji', 'oji'], ['ori', 'ori'], ['orm', 'orm'], ['osa', 'osa'], ['oss', 'oss'], ['ota', 'ota'], ['oto', 'oto'], ['paa', 'paa'], ['pag', 'pag'], ['pal', 'pal'], ['pam', 'pam'], ['pan', 'pan'], ['pap', 'pap'], ['pau', 'pau'], ['peo', 'peo'], ['phi', 'phi'], ['phn', 'phn'], ['pli', 'pli'], ['pol', 'pol'], ['pon', 'pon'], ['por', 'por'], ['pra', 'pra'], ['pro', 'pro'], ['pus', 'pus'], ['qaa-qtz', 'qaa-qtz'], ['que', 'que'], ['raj', 'raj'], ['rap', 'rap'], ['rar', 'rar'], ['roa', 'roa'], ['roh', 'roh'], ['rom', 'rom'], ['rum', 'rum'], ['run', 'run'], ['rup', 'rup'], ['rus', 'rus'], ['sad', 'sad'], ['sag', 'sag'], ['sah', 'sah'], ['sai', 'sai'], ['sal', 'sal'], ['sam', 'sam'], ['san', 'san'], ['sas', 'sas'], ['sat', 'sat'], ['scn', 'scn'], ['sco', 'sco'], ['sel', 'sel'], ['sem', 'sem'], ['sga', 'sga'], ['sgn', 'sgn'], ['shn', 'shn'], ['sid', 'sid'], ['sin', 'sin'], ['sio', 'sio'], ['sit', 'sit'], ['sla', 'sla'], ['slo', 'slo'], ['slv', 'slv'], ['sma', 'sma'], ['sme', 'sme'], ['smi', 'smi'], ['smj', 'smj'], ['smn', 'smn'], ['smo', 'smo'], ['sms', 'sms'], ['sna', 'sna'], ['snd', 'snd'], ['snk', 'snk'], ['sog', 'sog'], ['som', 'som'], ['son', 'son'], ['sot', 'sot'], ['spa', 'spa'], ['srd', 'srd'], ['srn', 'srn'], ['srp', 'srp'], ['srr', 'srr'], ['ssa', 'ssa'], ['ssw', 'ssw'], ['suk', 'suk'], ['sun', 'sun'], ['sus', 'sus'], ['sux', 'sux'], ['swa', 'swa'], ['swe', 'swe'], ['syc', 'syc'], ['syr', 'syr'], ['tah', 'tah'], ['tai', 'tai'], ['tam', 'tam'], ['tat', 'tat'], ['tel', 'tel'], ['tem', 'tem'], ['ter', 'ter'], ['tet', 'tet'], ['tgk', 'tgk'], ['tgl', 'tgl'], ['tha', 'tha'], ['tig', 'tig'], ['tir', 'tir'], ['tiv', 'tiv'], ['tkl', 'tkl'], ['tlh', 'tlh'], ['tli', 'tli'], ['tmh', 'tmh'], ['tog', 'tog'], ['ton', 'ton'], ['tpi', 'tpi'], ['tsi', 'tsi'], ['tsn', 'tsn'], ['tso', 'tso'], ['tuk', 'tuk'], ['tum', 'tum'], ['tup', 'tup'], ['tur', 'tur'], ['tut', 'tut'], ['tvl', 'tvl'], ['twi', 'twi'], ['tyv', 'tyv'], ['udm', 'udm'], ['uga', 'uga'], ['uig', 'uig'], ['ukr', 'ukr'], ['umb', 'umb'], ['und', 'und'], ['urd', 'urd'], ['uzb', 'uzb'], ['vai', 'vai'], ['ven', 'ven'], ['vie', 'vie'], ['vol', 'vol'], ['vot', 'vot'], ['wak', 'wak'], ['wal', 'wal'], ['war', 'war'], ['was', 'was'], ['wen', 'wen'], ['wln', 'wln'], ['wol', 'wol'], ['xal', 'xal'], ['xho', 'xho'], ['yao', 'yao'], ['yap', 'yap'], ['yid', 'yid'], ['yor', 'yor'], ['ypk', 'ypk'], ['zap', 'zap'], ['zbl', 'zbl'], ['zen', 'zen'], ['zgh', 'zgh'], ['zha', 'zha'], ['znd', 'znd'], ['zul', 'zul'], ['zun', 'zun'], ['zxx', 'zxx'], ['zza', 'zza'], ['multiple', 'multiple'], ['artificial', 'artificial'], ['other', 'other']], default=None, max_length=63, null=True)),
                ('point_of_disambiguation', models.IntegerField(default=None, null=True)),
                ('target_side', models.CharField(choices=[['left', 'left'], ['right', 'right']], default=None, max_length=255, null=True)),
                ('condition', models.CharField(default=None, max_length=255, null=True)),
                ('lab_trial_id', models.CharField(default=None, max_length=255, null=True)),
                ('aoi_region_set_id', models.ForeignKey(db_column='aoi_region_set_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='db.AOI_Region_Set')),
                ('dataset_id', models.ForeignKey(db_column='dataset_id', on_delete=django.db.models.deletion.CASCADE, to='db.Dataset')),
                ('distractor_id', models.ForeignKey(db_column='distractor_id', on_delete=django.db.models.deletion.CASCADE, related_name='distractor_stimulus', to='db.Stimulus')),
                ('target_id', models.ForeignKey(db_column='target_id', on_delete=django.db.models.deletion.CASCADE, related_name='target_stimulus', to='db.Stimulus')),
            ],
            options={
                'db_table': 'trial_types',
            },
        ),
        migrations.CreateModel(
            name='XY_Timepoint',
            fields=[
                ('xy_timepoint_id', models.IntegerField(primary_key=True, serialize=False)),
                ('x', models.IntegerField(default=None, null=True)),
                ('y', models.IntegerField(default=None, null=True)),
                ('t', models.IntegerField()),
                ('administration_id', models.ForeignKey(db_column='administration_id', on_delete=django.db.models.deletion.CASCADE, to='db.Administration')),
                ('trial_id', models.ForeignKey(db_column='trial_id', on_delete=django.db.models.deletion.CASCADE, to='db.Trial')),
            ],
            options={
                'db_table': 'xy_timepoints',
            },
        ),
        migrations.AddField(
            model_name='trial',
            name='trial_type_id',
            field=models.ForeignKey(db_column='trial_type_id', on_delete=django.db.models.deletion.CASCADE, to='db.Trial_Type'),
        ),
        migrations.AddField(
            model_name='aoi_timepoint',
            name='trial_id',
            field=models.ForeignKey(db_column='trial_id', on_delete=django.db.models.deletion.CASCADE, to='db.Trial'),
        ),
        migrations.AddField(
            model_name='administration',
            name='dataset_id',
            field=models.ForeignKey(db_column='dataset_id', on_delete=django.db.models.deletion.CASCADE, to='db.Dataset'),
        ),
        migrations.AddField(
            model_name='administration',
            name='subject_id',
            field=models.ForeignKey(db_column='subject_id', on_delete=django.db.models.deletion.CASCADE, to='db.Subject'),
        ),
    ]
