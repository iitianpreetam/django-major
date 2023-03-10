"""initial users info

Revision ID: af29fbec502d
Revises: 
Create Date: 2023-01-17 18:01:59.765290

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'af29fbec502d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courses',
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('course_name', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('course_id')
    )
    op.create_index(op.f('ix_courses_course_id'), 'courses', ['course_id'], unique=False)
    op.create_table('session_years',
    sa.Column('session_id', sa.Integer(), nullable=False),
    sa.Column('session_start_year', sa.String(length=12), nullable=False),
    sa.Column('session_end_year', sa.String(length=12), nullable=False),
    sa.PrimaryKeyConstraint('session_id')
    )
    op.create_index(op.f('ix_session_years_session_id'), 'session_years', ['session_id'], unique=False)
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=300), nullable=False),
    sa.Column('profile_picture', sa.String(length=300), nullable=True),
    sa.Column('dob', sa.String(length=10), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('address', mysql.LONGTEXT(), nullable=True),
    sa.Column('is_hod', mysql.TINYINT(), server_default=sa.text('0'), nullable=True),
    sa.Column('is_staff', mysql.TINYINT(), server_default=sa.text('0'), nullable=True),
    sa.Column('is_teacher', mysql.TINYINT(), server_default=sa.text('0'), nullable=True),
    sa.Column('is_student', mysql.TINYINT(), server_default=sa.text('0'), nullable=True),
    sa.Column('is_active', mysql.TINYINT(), server_default=sa.text('0'), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_user_id'), 'users', ['user_id'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('hods',
    sa.Column('hod_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('position', sa.String(length=50), nullable=False),
    sa.Column('education', mysql.LONGTEXT(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('hod_id')
    )
    op.create_index(op.f('ix_hods_hod_id'), 'hods', ['hod_id'], unique=False)
    op.create_index(op.f('ix_hods_user_id'), 'hods', ['user_id'], unique=False)
    op.create_table('staffs',
    sa.Column('staff_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('position', sa.String(length=50), nullable=False),
    sa.Column('education', mysql.LONGTEXT(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('staff_id')
    )
    op.create_index(op.f('ix_staffs_staff_id'), 'staffs', ['staff_id'], unique=False)
    op.create_index(op.f('ix_staffs_user_id'), 'staffs', ['user_id'], unique=False)
    op.create_table('students',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('session_under_id', sa.Integer(), nullable=True),
    sa.Column('courses_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.ForeignKeyConstraint(['courses_id'], ['courses.course_id'], ),
    sa.ForeignKeyConstraint(['session_under_id'], ['session_years.session_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('student_id')
    )
    op.create_index(op.f('ix_students_courses_id'), 'students', ['courses_id'], unique=False)
    op.create_index(op.f('ix_students_session_under_id'), 'students', ['session_under_id'], unique=False)
    op.create_index(op.f('ix_students_student_id'), 'students', ['student_id'], unique=False)
    op.create_index(op.f('ix_students_user_id'), 'students', ['user_id'], unique=False)
    op.create_table('teachers',
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('position', sa.String(length=50), nullable=False),
    sa.Column('education', mysql.LONGTEXT(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('teacher_id')
    )
    op.create_index(op.f('ix_teachers_teacher_id'), 'teachers', ['teacher_id'], unique=False)
    op.create_index(op.f('ix_teachers_user_id'), 'teachers', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_teachers_user_id'), table_name='teachers')
    op.drop_index(op.f('ix_teachers_teacher_id'), table_name='teachers')
    op.drop_table('teachers')
    op.drop_index(op.f('ix_students_user_id'), table_name='students')
    op.drop_index(op.f('ix_students_student_id'), table_name='students')
    op.drop_index(op.f('ix_students_session_under_id'), table_name='students')
    op.drop_index(op.f('ix_students_courses_id'), table_name='students')
    op.drop_table('students')
    op.drop_index(op.f('ix_staffs_user_id'), table_name='staffs')
    op.drop_index(op.f('ix_staffs_staff_id'), table_name='staffs')
    op.drop_table('staffs')
    op.drop_index(op.f('ix_hods_user_id'), table_name='hods')
    op.drop_index(op.f('ix_hods_hod_id'), table_name='hods')
    op.drop_table('hods')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_user_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_session_years_session_id'), table_name='session_years')
    op.drop_table('session_years')
    op.drop_index(op.f('ix_courses_course_id'), table_name='courses')
    op.drop_table('courses')
    # ### end Alembic commands ###
