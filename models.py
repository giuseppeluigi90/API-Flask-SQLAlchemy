from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Column, Integer, String, Float, JSON, DateTime
from sqlalchemy.orm import relationship

db = SQLAlchemy()

# Model for Account DB
class Account(db.Model):
    id = Column(Integer, primary_key = True)
    name = Column(String)
    address = Column(String)
    email = Column(String)

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email

# Model for Objectives DB
""" class Objectives(db.Model):
    id = Column(Integer, primary_key = True)
    name = Column(String)

    def __init__(self, name, address, email):
        self.name = name


# Model for ScrapersTasks DB
class Scrapers(db.Model):
    id = Column(Integer, primary_key = True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    objective_id = Column(Integer, ForeignKey('objectives.id'))
    target = Column(String)
    params = Column(JSON)
    scrapx = relationship("Objectives", back_populates = "scrapers")

    def __init__(self, created_at, updated_at, objective_id, target, params, scrapx):
        self.created_at = created_at
        self.updated_at = updated_at
        self.objective_id = objective_id
        self.target = target
        self.params = params
        self.scrapx = scrapx 


# Model for Scrapers Task DB
class ScrapersTasks(db.Model):
    id = Column(Integer, primary_key = True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    scraper_id = Column(Integer, ForeignKey('scrapers.id'))
    comment = Column(String)
    task_at = Column(DateTime)
    scraptk = relationship("Scrapers", back_populates = "scrapers_tasks")

    def __init__(self, created_at, updated_at, scraper_id, comment, task_at, scraptk):
        self.created_at = created_at
        self.updated_at = updated_at
        self.scraper_id = scraper_id
        self.comment = comment
        self.task_at = task_at
        self.scraptk = scraptk


# Model for Invoices DB
class Invoices(db.Model):
    id = Column(Integer, primary_key = True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    invoice_serial = Column(String)
    invoice_number = Column(Integer)
    invoice_amount = Column(Float)
    customer = relationship("Account", back_populates = "invoices")

    def __init__(self, create_at, updated_at, invoice_serial, invoice_number, invoice_amount, customer):
        self.create_at = created_at
        self.updated_at = updated_at
        self.invoice_serial = invoice_serial
        self.invoice_number = invoice_number
        self.invoice_amount = invoice_amount
        self.customer = customer

 """