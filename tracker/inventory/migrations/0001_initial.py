# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Shipment'
        db.create_table(u'inventory_shipment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('shipmentOpen', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'inventory', ['Shipment'])

        # Adding model 'Pallet'
        db.create_table(u'inventory_pallet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shipment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Shipment'])),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'inventory', ['Pallet'])

        # Adding model 'Donor'
        db.create_table(u'inventory_donor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('address', self.gf('django.db.models.fields.TextField')(max_length=300, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal(u'inventory', ['Donor'])

        # Adding model 'UserProfile'
        db.create_table(u'inventory_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'inventory', ['UserProfile'])

        # Adding model 'Device'
        db.create_table(u'inventory_device', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pallet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Pallet'], blank=True)),
            ('donor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Donor'])),
            ('manufacturer', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('deviceType', self.gf('django.db.models.fields.CharField')(default='DT', max_length=2)),
            ('deviceState', self.gf('django.db.models.fields.CharField')(default='RC', max_length=2)),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=500, blank=True)),
            ('license', self.gf('django.db.models.fields.TextField')(max_length=500, blank=True)),
        ))
        db.send_create_signal(u'inventory', ['Device'])

        # Adding model 'LogEntries'
        db.create_table(u'inventory_logentries', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('device', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Device'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('entryTime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'inventory', ['LogEntries'])

        # Adding model 'ActionPoint'
        db.create_table(u'inventory_actionpoint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('device', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Device'])),
            ('submitter', self.gf('django.db.models.fields.related.ForeignKey')(related_name='submitter', to=orm['auth.User'])),
            ('completer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='completer', blank=True, to=orm['auth.User'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('complete', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'inventory', ['ActionPoint'])


    def backwards(self, orm):
        # Deleting model 'Shipment'
        db.delete_table(u'inventory_shipment')

        # Deleting model 'Pallet'
        db.delete_table(u'inventory_pallet')

        # Deleting model 'Donor'
        db.delete_table(u'inventory_donor')

        # Deleting model 'UserProfile'
        db.delete_table(u'inventory_userprofile')

        # Deleting model 'Device'
        db.delete_table(u'inventory_device')

        # Deleting model 'LogEntries'
        db.delete_table(u'inventory_logentries')

        # Deleting model 'ActionPoint'
        db.delete_table(u'inventory_actionpoint')


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
            'completer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'completer'", 'blank': 'True', 'to': u"orm['auth.User']"}),
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
            'pallet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Pallet']", 'blank': 'True'})
        },
        u'inventory.donor': {
            'Meta': {'object_name': 'Donor'},
            'address': ('django.db.models.fields.TextField', [], {'max_length': '300', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'inventory.logentries': {
            'Meta': {'object_name': 'LogEntries'},
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'device': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Device']"}),
            'entryTime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
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