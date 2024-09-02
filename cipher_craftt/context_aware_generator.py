from .generator import generate_password

CONTEXT_POLICIES = {
    'finance': {'length': 16, 'use_upper': True, 'use_lower': True, 'use_digits': True, 'use_special': True},
    'social': {'length': 10, 'use_upper': True, 'use_lower': True, 'use_digits': True, 'use_special': False},
    'work': {'length': 12, 'use_upper': True, 'use_lower': True, 'use_digits': True, 'use_special': True},
    'gaming': {'length': 8, 'use_upper': False, 'use_lower': True, 'use_digits': True, 'use_special': False},
    'email': {'length': 14, 'use_upper': True, 'use_lower': True, 'use_digits': True, 'use_special': True},
    'banking': {'length': 20, 'use_upper': True, 'use_lower': True, 'use_digits': True, 'use_special': True},
    'shopping': {'length': 12, 'use_upper': True, 'use_lower': True, 'use_digits': True, 'use_special': False},
    'medical': {'length': 18, 'use_upper': True, 'use_lower': True, 'use_digits': True, 'use_special': True},
    'cloud': {'length': 16, 'use_upper': True, 'use_lower': True, 'use_digits': True, 'use_special': True},
    'secure': {'length': 24, 'use_upper': True, 'use_lower': True, 'use_digits': True, 'use_special': True},
}


def generate_context_aware_password(context):
    policy = CONTEXT_POLICIES.get(context.lower(), CONTEXT_POLICIES['work'])
    return generate_password(**policy)
