from __future__ import unicode_literals

from api.resources.group import GroupController
from api.resources.customer import CustomerIndexController, CustomerController
from api.resources.coupon import CouponIndexController, CouponController
from api.resources.plan import PlanIndexController, PlanController
from api.resources.payout import PayoutIndexController, PayoutController
from api.resources.plan_subscription import (PlanSubIndexController,
                                             PlanSubController)
from api.resources.payout_subscription import (PayoutSubIndexController,
                                               PayoutSubController)
from api.resources.plan_invoice import (PlanInvController,
                                        PlanInvIndexController)
from api.resources.payout_invoice import (PayoutInvController,
                                          PayoutInvIndexController)
from api.resources.plan_transaction import (PlanTransIndexController,
                                            PlanTransController)
from api.resources.payout_transaction import (PayoutTransIndexController,
                                              PayoutTransController)


def get_methods(controller):
    methods = ['GET', 'POST', 'PUT', 'DELETE']
    method_list = []
    for method in methods:
        if hasattr(controller, method.lower()):
            try:
                doc = getattr(controller, method.lower()).__doc__.strip()
                method_list.append({
                    'method': method,
                    'description': doc,
                })
            except AttributeError, e:
                print "ERROR {} has no doc.".format(getattr(controller,
                                                            method.lower()))
                raise e

    return method_list


def get_doc(obj):
    return None if not obj.__doc__ else ' '.join(obj.__doc__.split()).strip()


billy_spec = {
    'group': {
        'path': '/auth/',
        'controller': GroupController,
    },
    'customers_index': {
        'path': '/customer/',
        'controller': CustomerIndexController,
    },
    'customer': {
        'path': '/customer/<string:customer_id>/',
        'controller': CustomerController,
    },
    'coupon_index': {
        'path': '/coupon/',
        'controller': CouponIndexController,
    },
    'coupon': {
        'path': '/coupon/<string:coupon_id>/',
        'controller': CouponController,
    },
    'plan_index': {
        'path': '/plan/',
        'controller': PlanIndexController,
    },
    'plan': {
        'path': '/plan/<string:plan_id>/',
        'controller': PlanController,
    },
    'payout_index': {
        'path': '/payout/',
        'controller': PayoutIndexController,
    },
    'payout': {
        'path': '/payout/<string:payout_id>/',
        'controller': PayoutController,
    },
    'plan_subscription_index': {
        'path': '/plan_subscription/',
        'controller': PlanSubIndexController,
    },
    'plan_subscription': {
        'path': '/plan_subscription/<string:plan_sub_id>/',
        'controller': PlanSubController,
    },
    'payout_subscription_index': {
        'path': '/payout_subscription/',
        'controller': PayoutSubIndexController,
    },
    'payout_subscription': {
        'path': '/payout_subscription/<string:payout_sub_id>/',
        'controller': PayoutSubController,
    },
    'plan_invoice_index': {
        'path': '/plan_invoice/',
        'controller': PlanInvIndexController,
    },
    'plan_invoice': {
        'path': '/plan_invoice/<string:plan_inv_id>/',
        'controller': PlanInvController,
    },
    'payout_invoice_index': {
        'path': '/payout_invoice/',
        'controller': PayoutInvIndexController,
    },
    'payout_invoice': {
        'path': '/payout_invoice/<string:payout_inv_id>/',
        'controller': PayoutInvController,
    },
    'plan_transaction_index': {
        'path': '/plan_transaction/',
        'controller': PlanTransIndexController,
    },
    'plan_transaction': {
        'path': '/plan_transaction/<string:plan_trans_id>/',
        'controller': PlanTransController,
    },
    'payout_transaction_index': {
        'path': '/payout_transaction/',
        'controller': PayoutTransIndexController,
    },
    'payout_transaction': {
        'path': '/payout_transaction/<string:payout_trans_id>/',
        'controller': PayoutTransController,
    },

}

billy_spec_processed = {}
for resource, spec in billy_spec.iteritems():
    spec['methods'] = get_methods(spec['controller'])
    spec['description'] = get_doc(spec['controller'])
    spec = spec.copy()
    del spec['controller']
    billy_spec_processed[resource] = spec

if __name__ == '__main__':
    import json

    with open('spec.json', 'w+') as spec_file:
        json.dump(billy_spec_processed, spec_file, indent=4)
    print('Spec written successfully.')
