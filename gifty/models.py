from django.db import models


class FederalPublicUtilityCertificate(models.Model):
    """
    Defines a Federal Public Utility Certificate table
    """
    cnpj = models.CharField(max_length=15, null=False, blank=False)
    mj_process = models.CharField(max_length=15, null=False, blank=False)


class StatePublicUtilityCertificate(models.Model):
    """
    Defines a State Public Utility Certificate table
    """
    cnpj = models.CharField(max_length=15, null=False, blank=False)
    mj_process = models.CharField(max_length=15, null=False, blank=False)


class MunicipalPublicUtilityCertificate(models.Model):
    """
    Defines a Municipal Public Utility Certificate table
    """
    cnpj = models.CharField(max_length=15, null=False, blank=False)
    mj_process = models.CharField(max_length=15, null=False, blank=False)


class Ong(models.Model):
    """
    Defines a `ONG` table.
    """
    name = models.CharField(max_length=50, null=False, blank=False)
    federal_public_utility_certificate = models.ForeignKey(
        FederalPublicUtilityCertificate,
        on_delete=models.CASCADE,
        null=True
    )
    state_public_utility_certificate = models.ForeignKey(
        StatePublicUtilityCertificate,
        on_delete=models.CASCADE,
        null=True
    )
    municipal_public_utility_certificate = models.ForeignKey(
        MunicipalPublicUtilityCertificate,
        on_delete=models.CASCADE,
        null=True
    )
    phone_contact = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=50, null=False, blank=False)
    country = models.CharField(max_length=15, null=False, blank=False)
    state = models.CharField(max_length=50, null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    latitude = models.FloatField()
    longitude = models.FloatField()
    short_description = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    donation_link = models.TextField(null=True, blank=True)
