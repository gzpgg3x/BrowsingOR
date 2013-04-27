# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'questionsandanswers_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('publication_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'questionsandanswers', ['Question'])

        # Adding model 'Answer'
        db.create_table(u'questionsandanswers_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questionsandanswers.Question'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('best_answer', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'questionsandanswers', ['Answer'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'questionsandanswers_question')

        # Deleting model 'Answer'
        db.delete_table(u'questionsandanswers_answer')


    models = {
        u'questionsandanswers.answer': {
            'Meta': {'object_name': 'Answer'},
            'best_answer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['questionsandanswers.Question']"})
        },
        u'questionsandanswers.question': {
            'Meta': {'object_name': 'Question'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['questionsandanswers']