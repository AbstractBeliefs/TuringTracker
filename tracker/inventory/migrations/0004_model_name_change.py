# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'LogEntries'
        db.delete_table(u'inventory_logentries')

        # Adding model 'DevLogEntry'
        db.create_table(u'inventory_devlogentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('device', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Device'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('entryTime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'inventory', ['DevLogEntry'])


    def backwards(self, orm):
        # Adding model 'LogEntries'
        db.create_table(u'inventory_logentries', (
            ('entryTime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('device', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Device'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'inventory', ['LogEntries'])

        # Deleting model 'DevLogEntry'
        db.delete_table(u'inventory_devlogentry')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'inventory.actionpoint': {
            'Meta': {'object_name': 'ActionPoint'},
            'complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'completer': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'completer'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'device': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Device']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'submitter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'submitter'", 'to': u"orm['auth.User']"})
        },
        u'inventory.device': {
            'Meta': {'object_name': 'Device'},
            'deviceState': ('django.db.models.fields.CharField', [], {'default': "'RC'", 'max_length': '2'}),
            'deviceType': ('django.db.models.fields.CharField', [], {'default': "'DT'", 'max_length': '2'}),
            'donor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Donor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license': ('django.db.models.fields.TextField', [], {'max_length': '500', 'blank': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '500', 'blank': 'True'}),
            'pallet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Pallet']", 'null': 'True', 'blank': 'True'})
        },
        u'inventory.devlogentry': {
            'Meta': {'object_name': 'DevLogEntry'},
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'device': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Device']"}),
            'entryTime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'inventory.donor': {
            'Meta': {'object_name': 'Donor'},
            'address': ('django.db.models.fields.TextField', [], {'max_length': '300', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'inventory.pallet': {
            'Meta': {'object_name': 'Pallet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'shipment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Shipment']"})
        },
        u'inventory.shipment': {
            'Meta': {'object_name': 'Shipment'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shipmentOpen': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'inventory.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['inventory']