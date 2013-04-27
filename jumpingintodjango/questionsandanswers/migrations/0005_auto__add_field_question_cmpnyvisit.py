# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Question.cmpnyvisit'
        db.add_column(u'questionsandanswers_question', 'cmpnyvisit',
                      self.gf('django.db.models.fields.IntegerField')(default=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Question.cmpnyvisit'
        db.delete_column(u'questionsandanswers_question', 'cmpnyvisit')


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
            'cmpnyvisit': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'visit': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['questionsandanswers']