from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission, User


class Command(BaseCommand):
    help = 'Cria automaticamente os grupos e usuários de teste (nutri_teste e estagiario_teste)'

    def handle(self, *args, **kwargs):
        # 1. Grupo Nutricionista (acesso total ao cardápio e moderação de avaliações)
        grupo_nutri, _ = Group.objects.get_or_create(name='Nutricionista')
        perms_nutri = Permission.objects.filter(
            codename__in=[
                'add_cardapio', 'change_cardapio', 'delete_cardapio', 'view_cardapio',
                'view_avaliacao', 'delete_avaliacao',
            ]
        )
        grupo_nutri.permissions.set(perms_nutri)

        # 2. Grupo Estagiario_CAED (apenas visualização)
        grupo_estagiario, _ = Group.objects.get_or_create(name='Estagiario_CAED')
        perms_estagiario = Permission.objects.filter(
            codename__in=['view_cardapio', 'view_avaliacao']
        )
        grupo_estagiario.permissions.set(perms_estagiario)

        # 3. Usuário de teste: Nutricionista
        nutri, created_nutri = User.objects.get_or_create(username='nutri_teste')
        nutri.set_password('ifome123')
        nutri.is_staff = False
        nutri.is_superuser = False
        nutri.save()
        nutri.groups.set([grupo_nutri])

        # 4. Usuário de teste: Estagiário CAED
        estagiario, created_estagiario = User.objects.get_or_create(username='estagiario_teste')
        estagiario.set_password('ifome123')
        estagiario.is_staff = False
        estagiario.is_superuser = False
        estagiario.save()
        estagiario.groups.set([grupo_estagiario])

        self.stdout.write(self.style.SUCCESS(
            'Grupos e usuários criados! Logins: nutri_teste / estagiario_teste (senha: ifome123)'
        ))